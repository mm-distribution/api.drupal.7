# _field_ui_field_name_exists()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 722–729 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L722-L729)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_field_name_exists($value)
```

## Documentation

```text
Render API callback: Checks if a field machine name is taken.

@param $value
  The machine name, not prefixed with 'field_'.

@return
  Whether or not the field machine name is taken.
```

## Code

```php
function _field_ui_field_name_exists($value) {
  // Prefix with 'field_'.
  $field_name = 'field_' . $value;

  // We need to check inactive fields as well, so we can't use
  // field_info_fields().
  return (bool) field_read_fields(array('field_name' => $field_name), array('include_inactive' => TRUE));
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
