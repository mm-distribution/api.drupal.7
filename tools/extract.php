<?php
/**
 * @file
 * Extracts API documentation items from a Drupal 7 core checkout.
 *
 * Usage: php extract.php <drupal-root> > items.json
 *
 * Uses PHP's tokenizer so docblocks and code are taken verbatim from source.
 * Code is sliced as whole source lines, so it is an exact copy.
 */

$root = rtrim($argv[1] ?? '', '/');
if (!is_dir($root)) {
  fwrite(STDERR, "Usage: php extract.php <drupal-root>\n");
  exit(1);
}

$exts = ['php', 'module', 'inc', 'install', 'engine', 'theme', 'profile', 'test', 'sh'];
$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS));
$paths = [];
foreach ($it as $f) {
  $rel = substr($f->getPathname(), strlen($root) + 1);
  if (strpos($rel, '.git/') === 0) {
    continue;
  }
  if (in_array(strtolower($f->getExtension()), $exts, TRUE)) {
    $paths[] = $rel;
  }
}
sort($paths);

$out = ['files' => [], 'items' => [], 'groups' => []];

foreach ($paths as $rel) {
  $src = file_get_contents("$root/$rel");
  $lines = preg_split('/\R/', $src);
  $tokens = @token_get_all($src);
  $file = ['path' => $rel, 'doc' => NULL, 'doc_line' => NULL, 'lines' => count($lines)];

  // Group regions opened with @{ and closed with @}.
  $group_stack = [];
  $depth = 0;
  // Class context: [name, kind, depth at which body opened, docblock].
  $class = NULL;
  $last_doc = NULL;
  $last_doc_line = NULL;
  // Tokens allowed between a docblock and the thing it documents.
  $n = count($tokens);

  for ($i = 0; $i < $n; $i++) {
    $t = $tokens[$i];
    if (is_string($t)) {
      if ($t === '{') {
        $depth++;
      }
      elseif ($t === '}') {
        $depth--;
        if ($class && $depth < $class['open_depth']) {
          $class = NULL;
        }
      }
      elseif ($t !== '&') {
        $last_doc = NULL;
      }
      continue;
    }
    [$id, $text, $line] = $t;

    if ($id === T_CURLY_OPEN || $id === T_DOLLAR_OPEN_CURLY_BRACES) {
      $depth++;
      continue;
    }

    if ($id === T_DOC_COMMENT || $id === T_COMMENT) {
      // Group bookkeeping applies to any comment.
      if (preg_match('/@defgroup\s+(\S+)\s*(.*)$/m', $text, $m)) {
        $name = $m[1];
        if (!isset($out['groups'][$name])) {
          $out['groups'][$name] = ['name' => $name, 'title' => trim($m[2]), 'doc' => $text, 'file' => $rel, 'line' => $line];
        }
      }
      // Walk @{ and @} markers in order. @{ opens the most recently named
      // @defgroup/@addtogroup in this comment; @} closes the innermost group.
      if (preg_match_all('/@(defgroup|addtogroup)\s+(\S+)|@\{|@\}/', $text, $mm, PREG_SET_ORDER)) {
        $pending = NULL;
        foreach ($mm as $m) {
          if (!empty($m[2])) {
            $pending = $m[2];
          }
          elseif ($m[0] === '@{') {
            if ($pending !== NULL) {
              $group_stack[] = $pending;
              $pending = NULL;
            }
          }
          elseif ($m[0] === '@}') {
            array_pop($group_stack);
          }
        }
      }
      if ($id === T_DOC_COMMENT) {
        if ($file['doc'] === NULL && preg_match('/@file\b/', $text)) {
          $file['doc'] = $text;
          $file['doc_line'] = $line;
          $last_doc = NULL;
        }
        else {
          $last_doc = $text;
          $last_doc_line = $line;
        }
      }
      continue;
    }

    if (in_array($id, [T_WHITESPACE, T_ABSTRACT, T_FINAL, T_PUBLIC, T_PROTECTED, T_PRIVATE, T_STATIC, T_VAR], TRUE)) {
      continue;
    }

    // Classes and interfaces.
    if (($id === T_CLASS || $id === T_INTERFACE || (defined('T_TRAIT') && $id === T_TRAIT)) && $depth === 0) {
      $j = next_sig($tokens, $i);
      if ($j !== NULL && $tokens[$j][0] === T_STRING) {
        $name = $tokens[$j][1];
        $start = start_line($tokens, $i);
        $end = $start;
        $k = $i;
        // Find the opening brace.
        while ($k < $n && $tokens[$k] !== '{') {
          $k++;
        }
        $header = trim(implode("\n", array_slice($lines, $start - 1, line_of($tokens, $k) - $start + 1)));
        $kind = $id === T_CLASS ? 'class' : ($id === T_INTERFACE ? 'interface' : 'trait');
        $close = match_brace($tokens, $k);
        $end = line_of($tokens, $close);
        $out['items'][] = [
          'type' => $kind, 'name' => $name, 'file' => $rel, 'line' => $start, 'end_line' => $end,
          'doc' => $last_doc, 'doc_line' => $last_doc ? $last_doc_line : NULL, 'groups' => array_values(array_unique($group_stack)),
          'signature' => preg_replace('/\s*\{$/', '', $header),
        ];
        $class = ['name' => $name, 'kind' => $kind, 'open_depth' => $depth + 1];
        // Advance to the brace; its depth++ happens on the next loop pass.
        $i = $k - 1;
      }
      $last_doc = NULL;
      continue;
    }

    // Functions and methods (skip closures).
    if ($id === T_FUNCTION) {
      $j = next_sig($tokens, $i);
      if ($j !== NULL && is_amp($tokens[$j])) {
        $j = next_sig($tokens, $j);
      }
      $is_named = $j !== NULL && is_array($tokens[$j]) && $tokens[$j][0] === T_STRING;
      $in_class_body = $class && $depth === $class['open_depth'];
      if ($is_named && ($depth === 0 || $in_class_body)) {
        $name = $tokens[$j][1];
        $start = start_line($tokens, $i);
        // Body: first '{' or ';' after the parameter list.
        $k = $j;
        $paren = 0;
        while ($k < $n) {
          $tk = $tokens[$k];
          if ($tk === '(') {
            $paren++;
          }
          elseif ($tk === ')') {
            $paren--;
          }
          elseif ($paren === 0 && ($tk === '{' || $tk === ';')) {
            break;
          }
          $k++;
        }
        if ($tokens[$k] === '{') {
          $close = match_brace($tokens, $k);
          $end = line_of($tokens, $close);
          $sig_end = line_of($tokens, $k);
          $next = $close;
        }
        else {
          $end = line_of($tokens, $k);
          $sig_end = $end;
          $next = $k;
        }
        $sig = trim(implode("\n", array_slice($lines, $start - 1, $sig_end - $start + 1)));
        $sig = preg_replace('/\s*\{\s*$/', '', $sig);
        $item = [
          'type' => $in_class_body ? 'method' : 'function', 'name' => $name, 'file' => $rel,
          'line' => $start, 'end_line' => $end,
          'doc' => $last_doc, 'doc_line' => $last_doc ? $last_doc_line : NULL,
          'groups' => array_values(array_unique($group_stack)), 'signature' => $sig,
        ];
        if ($in_class_body) {
          $item['class'] = $class['name'];
        }
        $out['items'][] = $item;
        $i = $next;
        $last_doc = NULL;
        continue;
      }
      $last_doc = NULL;
      continue;
    }

    // define('CONSTANT', value);
    if ($id === T_STRING && strtolower($text) === 'define' && !$class) {
      $j = next_sig($tokens, $i);
      if ($j !== NULL && $tokens[$j] === '(') {
        $j2 = next_sig($tokens, $j);
        if ($j2 !== NULL && is_array($tokens[$j2]) && $tokens[$j2][0] === T_CONSTANT_ENCAPSED_STRING) {
          $name = trim($tokens[$j2][1], "'\"");
          $k = $j2;
          while ($k < $n && $tokens[$k] !== ';') {
            $k++;
          }
          $start = $line;
          $end = line_of($tokens, $k);
          $out['items'][] = [
            'type' => 'constant', 'name' => $name, 'file' => $rel, 'line' => $start, 'end_line' => $end,
            'doc' => $last_doc, 'doc_line' => $last_doc ? $last_doc_line : NULL,
            'groups' => array_values(array_unique($group_stack)),
            'signature' => trim(implode("\n", array_slice($lines, $start - 1, $end - $start + 1))),
          ];
          $i = $k;
        }
      }
      $last_doc = NULL;
      continue;
    }

    // Class constants.
    if ($id === T_CONST && $class && $depth === $class['open_depth']) {
      $j = next_sig($tokens, $i);
      $k = $i;
      while ($k < $n && $tokens[$k] !== ';') {
        $k++;
      }
      $start = start_line($tokens, $i);
      $end = line_of($tokens, $k);
      if ($j !== NULL && is_array($tokens[$j])) {
        $out['items'][] = [
          'type' => 'class_constant', 'name' => $tokens[$j][1], 'class' => $class['name'], 'file' => $rel,
          'line' => $start, 'end_line' => $end, 'doc' => $last_doc, 'doc_line' => $last_doc ? $last_doc_line : NULL,
          'groups' => [], 'signature' => trim(implode("\n", array_slice($lines, $start - 1, $end - $start + 1))),
        ];
      }
      $i = $k;
      $last_doc = NULL;
      continue;
    }

    // Class properties.
    if ($id === T_VARIABLE && $class && $depth === $class['open_depth']) {
      $k = $i;
      while ($k < $n && $tokens[$k] !== ';') {
        $k++;
      }
      $start = start_line($tokens, $i);
      $end = line_of($tokens, $k);
      $out['items'][] = [
        'type' => 'property', 'name' => $text, 'class' => $class['name'], 'file' => $rel,
        'line' => $start, 'end_line' => $end, 'doc' => $last_doc, 'doc_line' => $last_doc ? $last_doc_line : NULL,
        'groups' => [], 'signature' => trim(implode("\n", array_slice($lines, $start - 1, $end - $start + 1))),
      ];
      $i = $k;
      $last_doc = NULL;
      continue;
    }

    // Anything else breaks the association between a docblock and code.
    if (!in_array($id, [T_OPEN_TAG, T_CLOSE_TAG, T_INLINE_HTML], TRUE) || $id === T_INLINE_HTML) {
      $last_doc = NULL;
    }
  }

  $out['files'][] = $file;
}

$out['groups'] = array_values($out['groups']);
echo json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_INVALID_UTF8_SUBSTITUTE);

/**
 * Whether a token is a reference ampersand (string in PHP 7, token in PHP 8).
 */
function is_amp($t): bool {
  if ($t === '&') {
    return TRUE;
  }
  return is_array($t) && defined('T_AMPERSAND_NOT_FOLLOWED_BY_VAR_OR_VARARG')
    && in_array($t[0], [T_AMPERSAND_NOT_FOLLOWED_BY_VAR_OR_VARARG, T_AMPERSAND_FOLLOWED_BY_VAR_OR_VARARG], TRUE);
}

/**
 * Index of the next significant (non-whitespace, non-comment) token.
 */
function next_sig(array $tokens, int $i): ?int {
  $n = count($tokens);
  for ($j = $i + 1; $j < $n; $j++) {
    $t = $tokens[$j];
    if (is_array($t) && in_array($t[0], [T_WHITESPACE, T_COMMENT, T_DOC_COMMENT], TRUE)) {
      continue;
    }
    return $j;
  }
  return NULL;
}

/**
 * Line where a declaration starts, including leading modifiers.
 */
function start_line(array $tokens, int $i): int {
  $start = $tokens[$i][2];
  for ($j = $i - 1; $j >= 0; $j--) {
    $t = $tokens[$j];
    if (!is_array($t)) {
      break;
    }
    if ($t[0] === T_WHITESPACE) {
      continue;
    }
    if (in_array($t[0], [T_ABSTRACT, T_FINAL, T_PUBLIC, T_PROTECTED, T_PRIVATE, T_STATIC, T_VAR], TRUE)) {
      $start = $t[2];
      continue;
    }
    break;
  }
  return $start;
}

/**
 * Line number of token $k, computed for string tokens from neighbours.
 */
function line_of(array $tokens, int $k): int {
  for ($j = $k; $j >= 0; $j--) {
    if (is_array($tokens[$j])) {
      return $tokens[$j][2] + substr_count($tokens[$j][1], "\n") * ($j < $k ? 1 : 0);
    }
  }
  return 1;
}

/**
 * Index of the brace matching the '{' at $k.
 */
function match_brace(array $tokens, int $k): int {
  $n = count($tokens);
  $d = 0;
  for ($j = $k; $j < $n; $j++) {
    $t = $tokens[$j];
    if ($t === '{' || (is_array($t) && ($t[0] === T_CURLY_OPEN || $t[0] === T_DOLLAR_OPEN_CURLY_BRACES))) {
      $d++;
    }
    elseif ($t === '}') {
      $d--;
      if ($d === 0) {
        return $j;
      }
    }
  }
  return $n - 1;
}
