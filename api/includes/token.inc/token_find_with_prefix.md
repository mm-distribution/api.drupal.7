# token_find_with_prefix()

- **Type:** Function
- **File:** [`includes/token.inc`](_file.md), lines 219–228 · [local source](../../../source/includes/token.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/token.inc#L219-L228)

## Signature

```php
function token_find_with_prefix(array $tokens, $prefix, $delimiter = ':')
```

## Documentation

```text
Returns a list of tokens that begin with a specific prefix.

Used to extract a group of 'chained' tokens (such as [node:author:name])
from the full list of tokens found in text. For example:
@code
  $data = array(
    'author:name' => '[node:author:name]',
    'title'       => '[node:title]',
    'created'     => '[node:created]',
  );
  $results = token_find_with_prefix($data, 'author');
  $results == array('name' => '[node:author:name]');
@endcode

@param $tokens
  A keyed array of tokens, and their original raw form in the source text.
@param $prefix
  A textual string to be matched at the beginning of the token.
@param $delimiter
  An optional string containing the character that separates the prefix from
  the rest of the token. Defaults to ':'.

@return
  An associative array of discovered tokens, with the prefix and delimiter
  stripped from the key.
```

## Code

```php
function token_find_with_prefix(array $tokens, $prefix, $delimiter = ':') {
  $results = array();
  foreach ($tokens as $token => $raw) {
    $parts = explode($delimiter, $token, 2);
    if (count($parts) == 2 && $parts[0] == $prefix) {
      $results[$parts[1]] = $raw;
    }
  }
  return $results;
}
```

---
_Drupal 7.103 · [includes/token.inc](https://github.com/drupal/drupal/blob/7.103/includes/token.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
