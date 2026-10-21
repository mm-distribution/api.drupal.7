# field_ui_widget_type_form()

- **Type:** Function
- **File:** [`modules/field_ui/field_ui.admin.inc`](_file.md), lines 1666–1705 · [local source](../../../../source/modules/field_ui/field_ui.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc#L1666-L1705)
- **Module/theme:** field_ui
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function field_ui_widget_type_form($form, &$form_state, $instance)
```

## Documentation

```text
Form constructor for the widget selection form.

Path: BUNDLE_ADMIN_PATH/fields/%field/widget-type, where BUNDLE_ADMIN_PATH is
the path stored in the ['admin']['info'] property in the return value of
hook_entity_info().

@see field_ui_menu()
@see field_ui_widget_type_form_submit()
@ingroup forms
```

## Code

```php
function field_ui_widget_type_form($form, &$form_state, $instance) {
  drupal_set_title($instance['label']);

  $bundle = $instance['bundle'];
  $entity_type = $instance['entity_type'];
  $field_name = $instance['field_name'];

  $field = field_info_field($field_name);
  $field_type = field_info_field_types($field['type']);
  $widget_type = field_info_widget_types($instance['widget']['type']);
  $bundles = field_info_bundles();
  $bundle_label = $bundles[$entity_type][$bundle]['label'];

  $form = array(
    '#bundle' => $bundle,
    '#entity_type' => $entity_type,
    '#field_name' => $field_name,
  );

  $form['basic'] = array(
    '#type' => 'fieldset',
    '#title' => t('Change widget'),
  );
  $form['basic']['widget_type'] = array(
    '#type' => 'select',
    '#title' => t('Widget type'),
    '#required' => TRUE,
    '#options' => field_ui_widget_type_options($field['type']),
    '#default_value' => $instance['widget']['type'],
    '#description' => t('The type of form element you would like to present to the user when creating this field in the %type type.', array('%type' => $bundle_label)),
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Continue'));

  $form['#validate'] = array();
  $form['#submit'] = array('field_ui_widget_type_form_submit');

  return $form;
}
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
