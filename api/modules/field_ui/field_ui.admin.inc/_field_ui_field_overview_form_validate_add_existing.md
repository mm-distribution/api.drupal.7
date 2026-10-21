# _field_ui_field_overview_form_validate_add_existing()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 736–767 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L736-L767)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_field_overview_form_validate_add_existing($form, &$form_state)
```

## Documentation

```text
Validates the 'add existing field' row of field_ui_field_overview_form().

@see field_ui_field_overview_form_validate()
```

## Code

```php
function _field_ui_field_overview_form_validate_add_existing($form, &$form_state) {
  // The form element might be absent if no existing fields can be added to
  // this bundle.
  if (isset($form_state['values']['fields']['_add_existing_field'])) {
    $field = $form_state['values']['fields']['_add_existing_field'];

    // Validate if any information was provided in the 'add existing field' row.
    if (array_filter(array($field['label'], $field['field_name'], $field['widget_type']))) {
      // Missing label.
      if (!$field['label']) {
        form_set_error('fields][_add_existing_field][label', t('Add existing field: you need to provide a label.'));
      }

      // Missing existing field name.
      if (!$field['field_name']) {
        form_set_error('fields][_add_existing_field][field_name', t('Add existing field: you need to select a field.'));
      }

      // Missing widget type.
      if (!$field['widget_type']) {
        form_set_error('fields][_add_existing_field][widget_type', t('Add existing field: you need to select a widget.'));
      }
      // Wrong widget type.
      elseif ($field['field_name'] && ($existing_field = field_info_field($field['field_name']))) {
        $widget_types = field_ui_widget_type_options($existing_field['type']);
        if (!isset($widget_types[$field['widget_type']])) {
          form_set_error('fields][_add_existing_field][widget_type', t('Add existing field: invalid widget.'));
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
