# drupal_strtoupper()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 504–516 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L504-L516)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_strtoupper($text)
```

## Documentation

```text
Uppercase a UTF-8 string.

@param $text
  The string to run the operation on.

@return string
  The string in uppercase.

@ingroup php_wrappers
```

## Code

```php
function drupal_strtoupper($text) {
  global $multibyte;
  if ($multibyte == UNICODE_MULTIBYTE) {
    return mb_strtoupper($text);
  }
  else {
    // Use C-locale for ASCII-only uppercase
    $text = strtoupper($text);
    // Case flip Latin-1 accented letters
    $text = preg_replace_callback('/\xC3[\xA0-\xB6\xB8-\xBE]/', '_unicode_caseflip', $text);
    return $text;
  }
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
