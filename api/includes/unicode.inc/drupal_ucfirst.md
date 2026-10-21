# drupal_ucfirst()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 569–572 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L569-L572)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_ucfirst($text)
```

## Documentation

```text
Capitalizes the first letter of a UTF-8 string.

@param $text
  The string to convert.

@return
  The string with the first letter as uppercase.

@ingroup php_wrappers
```

## Code

```php
function drupal_ucfirst($text) {
  // Note: no mbstring equivalent!
  return drupal_strtoupper(drupal_substr($text, 0, 1)) . drupal_substr($text, 1);
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
