# field_ui_field_type_options()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1450–1467 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1450-L1467)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_type_options()
```

## Documentation

```text
Returns an array of field_type options.
```

## Code

```php
function field_ui_field_type_options() {
  $options = &drupal_static(__FUNCTION__);

  if (!isset($options)) {
    $options = array();
    $field_types = field_info_field_types();
    $field_type_options = array();
    foreach ($field_types as $name => $field_type) {
      // Skip field types which have no widget types, or should not be add via
      // uesr interface.
      if (field_ui_widget_type_options($name) && empty($field_type['no_ui'])) {
        $options[$name] = $field_type['label'];
      }
    }
    asort($options);
  }
  return $options;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
