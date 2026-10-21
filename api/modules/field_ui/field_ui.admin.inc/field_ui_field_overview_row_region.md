# field_ui_field_overview_row_region()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 98–108 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L98-L108)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_overview_row_region($row)
```

## Documentation

```text
Returns the region to which a row in the 'Manage fields' screen belongs.

This function is used as a #region_callback in
field_ui_field_overview_form(). It is called during
field_ui_table_pre_render().
```

## Code

```php
function field_ui_field_overview_row_region($row) {
  switch ($row['#row_type']) {
    case 'field':
    case 'extra_field':
      return 'main';
    case 'add_new_field':
      // If no input in 'label', assume the row has not been dragged out of the
      // 'add new' section.
      return (!empty($row['label']['#value']) ? 'main' : 'add_new');
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
