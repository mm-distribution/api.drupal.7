# _field_ui_reduce_order()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 79–89 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L79-L89)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_reduce_order($array, $a)
```

## Documentation

```text
Determines the rendering order of an array representing a tree.

Callback for array_reduce() within field_ui_table_pre_render().
```

## Code

```php
function _field_ui_reduce_order($array, $a) {
  $array = !isset($array) ? array() : $array;
  if ($a['name']) {
    $array[] = $a['name'];
  }
  if (!empty($a['children'])) {
    uasort($a['children'], 'drupal_sort_weight');
    $array = array_merge($array, array_reduce($a['children'], '_field_ui_reduce_order'));
  }
  return $array;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
