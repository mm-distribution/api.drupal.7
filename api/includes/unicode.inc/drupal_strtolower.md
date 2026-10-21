# drupal_strtolower()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 529–541 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L529-L541)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_strtolower($text)
```

## Documentation

```text
Lowercase a UTF-8 string.

@param $text
  The string to run the operation on.

@return string
  The string in lowercase.

@ingroup php_wrappers
```

## Code

```php
function drupal_strtolower($text) {
  global $multibyte;
  if ($multibyte == UNICODE_MULTIBYTE) {
    return mb_strtolower($text);
  }
  else {
    // Use C-locale for ASCII-only lowercase
    $text = strtolower($text);
    // Case flip Latin-1 accented letters
    $text = preg_replace_callback('/\xC3[\x80-\x96\x98-\x9E]/', '_unicode_caseflip', $text);
    return $text;
  }
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
