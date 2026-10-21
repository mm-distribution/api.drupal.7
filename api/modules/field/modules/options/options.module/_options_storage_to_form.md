# _options_storage_to_form()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 295–306 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L295-L306)
- **Module/theme:** options

## Signature

```php
function _options_storage_to_form($items, $options, $column, $properties)
```

## Documentation

```text
Transforms stored field values into the format the widgets need.
```

## Code

```php
function _options_storage_to_form($items, $options, $column, $properties) {
  $items_transposed = options_array_transpose($items);
  $values = (isset($items_transposed[$column]) && is_array($items_transposed[$column])) ? $items_transposed[$column] : array();

  // Discard values that are not in the current list of options. Flatten the
  // array if needed.
  if ($properties['optgroups']) {
    $options = options_array_flatten($options);
  }
  $values = array_values(array_intersect($values, array_keys($options)));
  return $values;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
