# _field_ui_field_overview_form_validate_add_new()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 671–711 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L671-L711)
- **Module/theme:** field_ui

## Signature

```php
function _field_ui_field_overview_form_validate_add_new($form, &$form_state)
```

## Documentation

```text
Validates the 'add new field' row of field_ui_field_overview_form().

@see field_ui_field_overview_form_validate()
```

## Code

```php
function _field_ui_field_overview_form_validate_add_new($form, &$form_state) {
  $field = $form_state['values']['fields']['_add_new_field'];

  // Validate if any information was provided in the 'add new field' row.
  if (array_filter(array($field['label'], $field['field_name'], $field['type'], $field['widget_type']))) {
    // Missing label.
    if (!$field['label']) {
      form_set_error('fields][_add_new_field][label', t('Add new field: you need to provide a label.'));
    }

    // Missing field name.
    if (!$field['field_name']) {
      form_set_error('fields][_add_new_field][field_name', t('Add new field: you need to provide a field name.'));
    }
    // Field name validation.
    else {
      $field_name = $field['field_name'];

      // Add the 'field_' prefix.
      $field_name = 'field_' . $field_name;
      form_set_value($form['fields']['_add_new_field']['field_name'], $field_name, $form_state);
    }

    // Missing field type.
    if (!$field['type']) {
      form_set_error('fields][_add_new_field][type', t('Add new field: you need to select a field type.'));
    }

    // Missing widget type.
    if (!$field['widget_type']) {
      form_set_error('fields][_add_new_field][widget_type', t('Add new field: you need to select a widget.'));
    }
    // Wrong widget type.
    elseif ($field['type']) {
      $widget_types = field_ui_widget_type_options($field['type']);
      if (!isset($widget_types[$field['widget_type']])) {
        form_set_error('fields][_add_new_field][widget_type', t('Add new field: invalid widget.'));
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
