# token_scan()

- **Type:** Function
- **File:** [`includes/token.inc`](_file.md), lines 114–138 · [local source](../../../source/includes/token.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/token.inc#L114-L138)

## Signature

```php
function token_scan($text)
```

## Documentation

```text
Builds a list of all token-like patterns that appear in the text.

@param $text
  The text to be scanned for possible tokens.

@return
  An associative array of discovered tokens, grouped by type.
```

## Code

```php
function token_scan($text) {
  // Matches tokens with the following pattern: [$type:$name]
  // $type and $name may not contain  [ ] characters.
  // $type may not contain : or whitespace characters, but $name may.
  preg_match_all('/
    \[             # [ - pattern start
    ([^\s\[\]:]*)  # match $type not containing whitespace : [ or ]
    :              # : - separator
    ([^\[\]]*)     # match $name not containing [ or ]
    \]             # ] - pattern end
    /x', $text, $matches);

  $types = $matches[1];
  $tokens = $matches[2];

  // Iterate through the matches, building an associative array containing
  // $tokens grouped by $types, pointing to the version of the token found in
  // the source text. For example, $results['node']['title'] = '[node:title]';
  $results = array();
  for ($i = 0; $i < count($tokens); $i++) {
    $results[$types[$i]][$tokens[$i]] = $matches[0][$i];
  }

  return $results;
}
```

---
_Drupal 7.103 · [includes/token.inc](https://github.com/drupal/drupal/blob/7.103/includes/token.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
