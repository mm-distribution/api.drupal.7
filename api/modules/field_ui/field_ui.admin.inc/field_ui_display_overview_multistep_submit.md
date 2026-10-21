# field_ui_display_overview_multistep_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1249–1284 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1249-L1284)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_display_overview_multistep_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for buttons in field_ui_display_overview_form().
```

## Code

```php
function field_ui_display_overview_multistep_submit($form, &$form_state) {
  $trigger = $form_state['triggering_element'];
  $op = $trigger['#op'];

  switch ($op) {
    case 'edit':
      // Store the field whose settings are currently being edited.
      $field_name = $trigger['#field_name'];
      $form_state['formatter_settings_edit'] = $field_name;
      break;

    case 'update':
      // Store the saved settings, and set the field back to 'non edit' mode.
      $field_name = $trigger['#field_name'];
      $values = $form_state['values']['fields'][$field_name]['settings_edit_form']['settings'];
      $form_state['formatter_settings'][$field_name] = $values;
      unset($form_state['formatter_settings_edit']);
      break;

    case 'cancel':
      // Set the field back to 'non edit' mode.
      unset($form_state['formatter_settings_edit']);
      break;

    case 'refresh_table':
      // If the currently edited field is one of the rows to be refreshed, set
      // it back to 'non edit' mode.
      $updated_rows = explode(' ', $form_state['values']['refresh_rows']);
      if (isset($form_state['formatter_settings_edit']) && in_array($form_state['formatter_settings_edit'], $updated_rows)) {
        unset($form_state['formatter_settings_edit']);
      }
      break;
  }

  $form_state['rebuild'] = TRUE;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
