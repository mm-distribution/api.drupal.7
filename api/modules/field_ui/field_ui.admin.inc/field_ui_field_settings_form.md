# field_ui_field_settings_form()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1577–1626 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1577-L1626)
- **Module/theme:** field_ui
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function field_ui_field_settings_form($form, &$form_state, $instance)
```

## Documentation

```text
Form constructor for the field settings edit page.

@see field_ui_field_settings_form_submit()
@ingroup forms
```

## Code

```php
function field_ui_field_settings_form($form, &$form_state, $instance) {
  $bundle = $instance['bundle'];
  $entity_type = $instance['entity_type'];
  $field = field_info_field($instance['field_name']);

  drupal_set_title($instance['label']);

  $description = '<p>' . t('These settings apply to the %field field everywhere it is used. These settings impact the way that data is stored in the database and cannot be changed once data has been created.', array('%field' => $instance['label'])) . '</p>';

  // Create a form structure for the field values.
  $form['field'] = array(
    '#type' => 'fieldset',
    '#title' => t('Field settings'),
    '#description' => $description,
    '#tree' => TRUE,
  );

  // See if data already exists for this field.
  // If so, prevent changes to the field settings.
  $has_data = field_has_data($field);
  if ($has_data) {
    $form['field']['#description'] = '<div class="messages error">' . t('There is data for this field in the database. The field settings can no longer be changed.') . '</div>' . $form['field']['#description'];
  }

  // Build the non-configurable field values.
  $form['field']['field_name'] = array('#type' => 'value', '#value' => $field['field_name']);
  $form['field']['type'] = array('#type' => 'value', '#value' => $field['type']);
  $form['field']['module'] = array('#type' => 'value', '#value' => $field['module']);
  $form['field']['active'] = array('#type' => 'value', '#value' => $field['active']);

  // Add settings provided by the field module. The field module is
  // responsible for not returning settings that cannot be changed if
  // the field already has data.
  $form['field']['settings'] = array();
  $additions = module_invoke($field['module'], 'field_settings_form', $field, $instance, $has_data);
  if (is_array($additions)) {
    $form['field']['settings'] = $additions;
  }
  if (empty($form['field']['settings'])) {
    $form['field']['settings'] = array(
      '#markup' => t('%field has no field settings.', array('%field' => $instance['label'])),
    );
  }
  $form['#entity_type'] = $entity_type;
  $form['#bundle'] = $bundle;

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save field settings'));
  return $form;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
