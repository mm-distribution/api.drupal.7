# _field_sort_items_value_helper()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 549–553 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L549-L553)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_sort_items_value_helper($a, $b)
```

## Documentation

```text
Same as above, using ['_weight']['#value']
```

## Code

```php
function _field_sort_items_value_helper($a, $b) {
  $a_weight = (is_array($a) && isset($a['_weight']['#value']) ? $a['_weight']['#value'] : 0);
  $b_weight = (is_array($b) && isset($b['_weight']['#value']) ? $b['_weight']['#value'] : 0);
  return $a_weight - $b_weight;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
