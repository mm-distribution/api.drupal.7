# search_excerpt()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1127–1258 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1127-L1258)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md)

## Signature

```php
function search_excerpt($keys, $text)
```

## Documentation

```text
Returns snippets from a piece of text, with certain keywords highlighted.
Used for formatting search results.

@param $keys
  A string containing a search query.

@param $text
  The text to extract fragments from.

@return
  A string containing HTML for the excerpt.
```

## Code

```php
function search_excerpt($keys, $text) {
  // We highlight around non-indexable or CJK characters.
  $boundary = '(?:(?<=[' . PREG_CLASS_UNICODE_WORD_BOUNDARY . PREG_CLASS_CJK . '])|(?=[' . PREG_CLASS_UNICODE_WORD_BOUNDARY . PREG_CLASS_CJK . ']))';

  // Extract positive keywords and phrases
  preg_match_all('/ ("([^"]+)"|(?!OR)([^" ]+))/', ' ' . $keys, $matches);
  $keys = array_merge($matches[2], $matches[3]);

  // Prepare text by stripping HTML tags and decoding HTML entities.
  $text = strip_tags(str_replace(array('<', '>'), array(' <', '> '), $text));
  $text = decode_entities($text);

  // Slash-escape quotes in the search keyword string.
  array_walk($keys, '_search_excerpt_replace');
  $workkeys = $keys;

  // Extract fragments around keywords.
  // First we collect ranges of text around each keyword, starting/ending
  // at spaces, trying to get to 256 characters.
  // If the sum of all fragments is too short, we look for second occurrences.
  $ranges = array();
  $included = array();
  $foundkeys = array();
  $length = 0;
  while ($length < 256 && count($workkeys)) {
    foreach ($workkeys as $k => $key) {
      if (strlen($key) == 0) {
        unset($workkeys[$k]);
        unset($keys[$k]);
        continue;
      }
      if ($length >= 256) {
        break;
      }
      // Remember occurrence of key so we can skip over it if more occurrences
      // are desired.
      if (!isset($included[$key])) {
        $included[$key] = 0;
      }
      // Locate a keyword (position $p, always >0 because $text starts with a
      // space). First try bare keyword, but if that doesn't work, try to find a
      // derived form from search_simplify().
      $p = 0;
      if (preg_match('/' . $boundary . $key . $boundary . '/iu', $text, $match, PREG_OFFSET_CAPTURE, $included[$key])) {
        $p = $match[0][1];
      }
      else {
        $info = search_simplify_excerpt_match($key, $text, $included[$key], $boundary);
        if (isset($info['where'])) {
          $p = $info['where'];
          if ($info['keyword']) {
            $foundkeys[] = $info['keyword'];
          }
        }
      }
      // Now locate a space in front (position $q) and behind it (position $s),
      // leaving about 60 characters extra before and after for context.
      // Note that a space was added to the front and end of $text above.
      if ($p) {
        if (($q = strpos(' ' . $text, ' ', max(0, $p - 61))) !== FALSE) {
          $end = substr($text . ' ', $p, 80);
          if (($s = strrpos($end, ' ')) !== FALSE) {
            // Account for the added spaces.
            $q = max($q - 1, 0);
            $s = min($s, strlen($end) - 1);
            $ranges[$q] = $p + $s;
            $length += $p + $s - $q;
            $included[$key] = $p + 1;
          }
          else {
            unset($workkeys[$k]);
          }
        }
        else {
          unset($workkeys[$k]);
        }
      }
      else {
        unset($workkeys[$k]);
      }
    }
  }

  if (count($ranges) == 0) {
    // We didn't find any keyword matches, so just return the first part of the
    // text. We also need to re-encode any HTML special characters that we
    // entity-decoded above.
    return check_plain(truncate_utf8($text, 256, TRUE, TRUE));
  }

  // Sort the text ranges by starting position.
  ksort($ranges);

  // Now we collapse overlapping text ranges into one. The sorting makes it O(n).
  $newranges = array();
  foreach ($ranges as $from2 => $to2) {
    if (!isset($from1)) {
      $from1 = $from2;
      $to1 = $to2;
      continue;
    }
    if ($from2 <= $to1) {
      $to1 = max($to1, $to2);
    }
    else {
      $newranges[$from1] = $to1;
      $from1 = $from2;
      $to1 = $to2;
    }
  }
  $newranges[$from1] = $to1;

  // Fetch text
  $out = array();
  foreach ($newranges as $from => $to) {
    $out[] = substr($text, $from, $to - $from);
  }

  // Let translators have the ... separator text as one chunk.
  $dots = explode('!excerpt', t('... !excerpt ... !excerpt ...'));

  $text = (isset($newranges[0]) ? '' : $dots[0]) . implode($dots[1], $out) . $dots[2];
  $text = check_plain($text);

  // Slash-escape quotes in keys found in a derived form and merge with original keys.
  array_walk($foundkeys, '_search_excerpt_replace');
  $keys = array_merge($keys, $foundkeys);

  // Highlight keywords. Must be done at once to prevent conflicts ('strong' and '<strong>').
  $text = preg_replace('/' . $boundary . '(' . implode('|', $keys) . ')' . $boundary . '/iu', '<strong>\0</strong>', $text);
  return $text;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
