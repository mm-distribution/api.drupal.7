# field_ui_field_edit_form_validate()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 2026–2056 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L2026-L2056)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_edit_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for field_ui_field_edit_form().

@see field_ui_field_edit_form_submit().
```

## Code

```php
function field_ui_field_edit_form_validate($form, &$form_state) {
  // Take the incoming values as the $instance definition, so that the 'default
  // value' gets validated using the instance settings being submitted.
  $instance = $form_state['values']['instance'];
  $field_name = $instance['field_name'];

  if (isset($form['instance']['default_value_widget'])) {
    $element = $form['instance']['default_value_widget'];

    $field_state = field_form_get_state($element['#parents'], $field_name, LANGUAGE_NONE, $form_state);
    $field = $field_state['field'];

    // Extract the 'default value'.
    $items = array();
    field_default_extract_form_values(NULL, NULL, $field, $instance, LANGUAGE_NONE, $items, $element, $form_state);

    // Validate the value and report errors.
    $errors = array();
    $function = $field['module'] . '_field_validate';
    if (function_exists($function)) {
      $function(NULL, NULL, $field, $instance, LANGUAGE_NONE, $items, $errors);
    }
    if (isset($errors[$field_name][LANGUAGE_NONE])) {
      // Store reported errors in $form_state.
      $field_state['errors'] = $errors[$field_name][LANGUAGE_NONE];
      field_form_set_state($element['#parents'], $field_name, LANGUAGE_NONE, $form_state, $field_state);
      // Assign reported errors to the correct form element.
      field_default_form_errors(NULL, NULL, $field, $instance, LANGUAGE_NONE, $items, $element, $form_state);
    }
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
