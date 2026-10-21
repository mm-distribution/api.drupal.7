# element_property()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6723–6725 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6723-L6725)

## Signature

```php
function element_property($key)
```

## Documentation

```text
Checks if the key is a property.
```

## Code

```php
function element_property($key) {
  return $key !== '' && is_string($key) && $key[0] == '#';
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
