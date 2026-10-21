# element_properties()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6730–6732 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6730-L6732)

## Signature

```php
function element_properties($element)
```

## Documentation

```text
Gets properties of a structured array element (keys beginning with '#').
```

## Code

```php
function element_properties($element) {
  return array_filter(array_keys((array) $element), 'element_property');
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
