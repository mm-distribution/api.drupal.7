# field_ui_widget_type_form_submit()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1710–1735 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1710-L1735)
- **Module/theme:** field_ui

## Signature

```php
function field_ui_widget_type_form_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for field_ui_widget_type_form().
```

## Code

```php
function field_ui_widget_type_form_submit($form, &$form_state) {
  $form_values = $form_state['values'];
  $bundle = $form['#bundle'];
  $entity_type = $form['#entity_type'];
  $field_name = $form['#field_name'];

  // Retrieve the stored instance settings to merge with the incoming values.
  $instance = field_read_instance($entity_type, $field_name, $bundle);

  // Set the right module information.
  $widget_type = field_info_widget_types($form_values['widget_type']);
  $widget_module = $widget_type['module'];

  $instance['widget']['type'] = $form_values['widget_type'];
  $instance['widget']['module'] = $widget_module;

  try {
    field_update_instance($instance);
    drupal_set_message(t('Changed the widget for field %label.', array('%label' => $instance['label'])));
  }
  catch (Exception $e) {
    drupal_set_message(t('There was a problem changing the widget for field %label.', array('%label' => $instance['label'])), 'error');
  }

  $form_state['redirect'] = field_ui_next_destination($entity_type, $bundle);
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
