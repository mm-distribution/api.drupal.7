# field_ui_field_overview_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 774–884 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L774-L884)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_field_overview_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for field_ui_field_overview_form().

@see field_ui_field_overview_form_validate()
```

## Code

```php
function field_ui_field_overview_form_submit($form, &$form_state) {
  $form_values = $form_state['values']['fields'];
  $entity_type = $form['#entity_type'];
  $bundle = $form['#bundle'];
  $admin_path = _field_ui_bundle_admin_path($entity_type, $bundle);

  $bundle_settings = field_bundle_settings($entity_type, $bundle);

  // Update field weights.
  foreach ($form_values as $key => $values) {
    if (in_array($key, $form['#fields'])) {
      $instance = field_read_instance($entity_type, $key, $bundle);
      $instance['widget']['weight'] = $values['weight'];
      field_update_instance($instance);
    }
    elseif (in_array($key, $form['#extra'])) {
      $bundle_settings['extra_fields']['form'][$key]['weight'] = $values['weight'];
    }
  }

  field_bundle_settings($entity_type, $bundle, $bundle_settings);

  $destinations = array();

  // Check if the target entity uses a non numeric ID.
  $entity_info = entity_get_info($entity_type);
  if (!empty($entity_info['entity_id_type']) && $entity_info['entity_id_type'] === 'string') {
    $entity_id_type = 'string';
  } else {
    $entity_id_type = NULL;
  }

  // Create new field.
  $field = array();
  if (!empty($form_values['_add_new_field']['field_name'])) {
    $values = $form_values['_add_new_field'];

    $field = array(
      'field_name' => $values['field_name'],
      'type' => $values['type'],
      'translatable' => $values['translatable'],
      'entity_id_type' => $entity_id_type,
    );
    $instance = array(
      'field_name' => $field['field_name'],
      'entity_type' => $entity_type,
      'bundle' => $bundle,
      'label' => $values['label'],
      'widget' => array(
        'type' => $values['widget_type'],
        'weight' => $values['weight'],
      ),
    );

    // Create the field and instance.
    try {
      field_create_field($field);
      field_create_instance($instance);

      $destinations[] = $admin_path . '/fields/' . $field['field_name'] . '/field-settings';
      $destinations[] = $admin_path . '/fields/' . $field['field_name'];

      // Store new field information for any additional submit handlers.
      $form_state['fields_added']['_add_new_field'] = $field['field_name'];
    }
    catch (Exception $e) {
      drupal_set_message(t('There was a problem creating field %label: !message', array('%label' => $instance['label'], '!message' => $e->getMessage())), 'error');
    }
  }

  // Add existing field.
  if (!empty($form_values['_add_existing_field']['field_name'])) {
    $values = $form_values['_add_existing_field'];
    $field = field_info_field($values['field_name']);
    if (!empty($field['locked'])) {
      drupal_set_message(t('The field %label cannot be added because it is locked.', array('%label' => $values['label'])), 'error');
    }
    else {
      $instance = array(
        'field_name' => $field['field_name'],
        'entity_type' => $entity_type,
        'bundle' => $bundle,
        'label' => $values['label'],
        'widget' => array(
          'type' => $values['widget_type'],
          'weight' => $values['weight'],
        ),
      );

      try {
        field_create_instance($instance);
        $destinations[] = $admin_path . '/fields/' . $instance['field_name'] . '/edit';
        // Store new field information for any additional submit handlers.
        $form_state['fields_added']['_add_existing_field'] = $instance['field_name'];
      }
      catch (Exception $e) {
        drupal_set_message(t('There was a problem creating field instance %label: @message.', array('%label' => $instance['label'], '@message' => $e->getMessage())), 'error');
      }
    }
  }

  if ($destinations) {
    $destination = drupal_get_destination();
    $destinations[] = $destination['destination'];
    unset($_GET['destination']);
    $form_state['redirect'] = field_ui_get_destinations($destinations);
  }
  else {
    drupal_set_message(t('Your settings have been saved.'));
  }
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
