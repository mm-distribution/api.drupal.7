# field_ui_display_overview_row_region()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 117–123 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L117-L123)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_display_overview_row_region($row)
```

## Documentation

```text
Returns the region to which a row in the 'Manage display' screen belongs.

This function is used as a #region_callback in
field_ui_field_overview_form(), and is called during
field_ui_table_pre_render().
```

## Code

```php
function field_ui_display_overview_row_region($row) {
  switch ($row['#row_type']) {
    case 'field':
    case 'extra_field':
      return ($row['format']['type']['#value'] == 'hidden' ? 'hidden' : 'visible');
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
