# drupal_json_decode()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5308–5310 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5308-L5310)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_json_decode($var)
```

## Documentation

```text
Converts an HTML-safe JSON string into its PHP equivalent.

@see drupal_json_encode()
@ingroup php_wrappers
```

## Code

```php
function drupal_json_decode($var) {
  return json_decode($var, TRUE);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
