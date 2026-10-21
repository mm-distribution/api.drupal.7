# field_ui_field_edit_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 2063–2098 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L2063-L2098)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_edit_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for field_ui_field_edit_form().

@see field_ui_field_edit_form_validate().
```

## Code

```php
function field_ui_field_edit_form_submit($form, &$form_state) {
  $instance = $form_state['values']['instance'];
  $field = $form_state['values']['field'];

  // Update any field settings that have changed.
  $field_source = field_info_field($instance['field_name']);
  $field = array_merge($field_source, $field);
  try {
    field_update_field($field);
  }
  catch (Exception $e) {
    drupal_set_message(t('Attempt to update field %label failed: %message.', array('%label' => $instance['label'], '%message' => $e->getMessage())), 'error');
    return;
  }

  // Handle the default value.
  if (isset($form['instance']['default_value_widget'])) {
    $element = $form['instance']['default_value_widget'];

    // Extract field values.
    $items = array();
    field_default_extract_form_values(NULL, NULL, $field, $instance, LANGUAGE_NONE, $items, $element, $form_state);
    field_default_submit(NULL, NULL, $field, $instance, LANGUAGE_NONE, $items, $element, $form_state);

    $instance['default_value'] = $items ? $items : NULL;
  }

  // Retrieve the stored instance settings to merge with the incoming values.
  $instance_source = field_read_instance($instance['entity_type'], $instance['field_name'], $instance['bundle']);
  $instance = array_merge($instance_source, $instance);
  field_update_instance($instance);

  drupal_set_message(t('Saved %label configuration.', array('%label' => $instance['label'])));

  $form_state['redirect'] = field_ui_next_destination($instance['entity_type'], $instance['bundle']);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
