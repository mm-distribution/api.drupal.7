# _field_sort_items()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 524–534 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L524-L534)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_sort_items($field, $items)
```

## Documentation

```text
Helper function to sort items in a field according to
user drag-n-drop reordering.
```

## Code

```php
function _field_sort_items($field, $items) {
  if (($field['cardinality'] > 1 || $field['cardinality'] == FIELD_CARDINALITY_UNLIMITED) && isset($items[0]['_weight'])) {
    usort($items, '_field_sort_items_helper');
    foreach ($items as $delta => $item) {
      if (is_array($items[$delta])) {
        unset($items[$delta]['_weight']);
      }
    }
  }
  return $items;
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
