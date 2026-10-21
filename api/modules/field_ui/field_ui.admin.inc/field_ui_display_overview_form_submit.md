# field_ui_display_overview_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1327–1400 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1327-L1400)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_display_overview_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for field_ui_display_overview_form().
```

## Code

```php
function field_ui_display_overview_form_submit($form, &$form_state) {
  $form_values = $form_state['values'];
  $entity_type = $form['#entity_type'];
  $bundle = $form['#bundle'];
  $view_mode = $form['#view_mode'];

  // Save data for 'regular' fields.
  foreach ($form['#fields'] as $field_name) {
    // Retrieve the stored instance settings to merge with the incoming values.
    $instance = field_read_instance($entity_type, $field_name, $bundle);
    $values = $form_values['fields'][$field_name];
    // Get formatter settings. They lie either directly in submitted form
    // values (if the whole form was submitted while some formatter
    // settings were being edited), or have been persisted in
    // $form_state.
    $settings = array();
    if (isset($values['settings_edit_form']['settings'])) {
      $settings = $values['settings_edit_form']['settings'];
    }
    elseif (isset($form_state['formatter_settings'][$field_name])) {
      $settings = $form_state['formatter_settings'][$field_name];
    }
    elseif (isset($instance['display'][$view_mode]['settings'])) {
      $settings = $instance['display'][$view_mode]['settings'];
    }

    // Only save settings actually used by the selected formatter.
    $default_settings = field_info_formatter_settings($values['type']);
    $settings = array_intersect_key($settings, $default_settings);

    $instance['display'][$view_mode] = array(
      'label' => $values['label'],
      'type' => $values['type'],
      'weight' => $values['weight'],
      'settings' => $settings,
    );
    field_update_instance($instance);
  }

  // Get current bundle settings.
  $bundle_settings = field_bundle_settings($entity_type, $bundle);

  // Save data for 'extra' fields.
  foreach ($form['#extra'] as $name) {
    $bundle_settings['extra_fields']['display'][$name][$view_mode] = array(
      'weight' => $form_values['fields'][$name]['weight'],
      'visible' => $form_values['fields'][$name]['type'] == 'visible',
    );
  }

  // Save view modes data.
  if ($view_mode == 'default') {
    $entity_info = entity_get_info($entity_type);
    foreach ($form_values['view_modes_custom'] as $view_mode_name => $value) {
      // Display a message for each view mode newly configured to use custom
      // settings.
      $view_mode_settings = field_view_mode_settings($entity_type, $bundle);
      if (!empty($value) && empty($view_mode_settings[$view_mode_name]['custom_settings'])) {
        $view_mode_label = $entity_info['view modes'][$view_mode_name]['label'];
        $path = _field_ui_bundle_admin_path($entity_type, $bundle) . "/display/$view_mode_name";
        drupal_set_message(t('The %view_mode mode now uses custom display settings. You might want to <a href="@url">configure them</a>.', array('%view_mode' => $view_mode_label, '@url' => url($path))));
        // Initialize the newly customized view mode with the display settings
        // from the default view mode.
        _field_ui_add_default_view_mode_settings($entity_type, $bundle, $view_mode_name, $bundle_settings);
      }
      $bundle_settings['view_modes'][$view_mode_name]['custom_settings'] = !empty($value);
    }
  }

  // Save updated bundle settings.
  field_bundle_settings($entity_type, $bundle, $bundle_settings);

  drupal_set_message(t('Your settings have been saved.'));
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
