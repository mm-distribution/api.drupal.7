# _field_sort_items_helper()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 540–544 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L540-L544)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_sort_items_helper($a, $b)
```

## Documentation

```text
Sort function for items order.
(copied form element_sort(), which acts on #weight keys)
```

## Code

```php
function _field_sort_items_helper($a, $b) {
  $a_weight = (is_array($a) ? $a['_weight'] : 0);
  $b_weight = (is_array($b) ? $b['_weight'] : 0);
  return $a_weight - $b_weight;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
