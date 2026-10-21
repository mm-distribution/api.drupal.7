# field_ui_field_settings_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1631–1653 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1631-L1653)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_settings_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for field_ui_field_settings_form().
```

## Code

```php
function field_ui_field_settings_form_submit($form, &$form_state) {
  $form_values = $form_state['values'];
  $field_values = $form_values['field'];

  // Merge incoming form values into the existing field.
  $field = field_info_field($field_values['field_name']);

  $entity_type = $form['#entity_type'];
  $bundle = $form['#bundle'];
  $instance = field_info_instance($entity_type, $field['field_name'], $bundle);

  // Update the field.
  $field = array_merge($field, $field_values);

  try {
    field_update_field($field);
    drupal_set_message(t('Updated field %label field settings.', array('%label' => $instance['label'])));
    $form_state['redirect'] = field_ui_next_destination($entity_type, $bundle);
  }
  catch (Exception $e) {
    drupal_set_message(t('Attempt to update field %label failed: %message.', array('%label' => $instance['label'], '%message' => $e->getMessage())), 'error');
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
