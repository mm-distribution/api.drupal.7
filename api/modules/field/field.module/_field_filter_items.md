# _field_filter_items()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 509–518 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L509-L518)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_filter_items($field, $items)
```

## Documentation

```text
Helper function to filter out empty field values.

@param $field
  The field definition.
@param $items
  The field values to filter.

@return
  The array of items without empty field values. The function also renumbers
  the array keys to ensure sequential deltas.
```

## Code

```php
function _field_filter_items($field, $items) {
  $function = $field['module'] . '_field_is_empty';
  foreach ((array) $items as $delta => $item) {
    // Explicitly break if the function is undefined.
    if ($function($item, $field)) {
      unset($items[$delta]);
    }
  }
  return array_values($items);
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
