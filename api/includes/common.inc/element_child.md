# element_child()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6737–6739 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6737-L6739)

## Signature

```php
function element_child($key)
```

## Documentation

```text
Checks if the key is a child.
```

## Code

```php
function element_child($key) {
  return !isset($key[0]) || $key[0] != '#';
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
