# drupal_strlen()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 479–491 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L479-L491)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_strlen($text)
```

## Documentation

```text
Counts the number of characters in a UTF-8 string.

This is less than or equal to the byte count.

@param $text
  The string to run the operation on.

@return integer
  The length of the string.

@ingroup php_wrappers
```

## Code

```php
function drupal_strlen($text) {
  global $multibyte;
  if (is_null($text)) {
    return 0;
  }
  if ($multibyte == UNICODE_MULTIBYTE) {
    return mb_strlen($text);
  }
  else {
    // Do not count UTF-8 continuation bytes.
    return strlen(preg_replace("/[\x80-\xBF]/", '', $text));
  }
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
