# field_test_field_widget_settings_form()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 245–258 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L245-L258)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_settings_form()](../../../field_ui/field_ui.api.php/hook_field_widget_settings_form.md)

## Signature

```php
function field_test_field_widget_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_widget_settings_form().
```

## Code

```php
function field_test_field_widget_settings_form($field, $instance) {
  $widget = $instance['widget'];
  $settings = $widget['settings'];

  $form['test_widget_setting'] = array(
    '#type' => 'textfield',
    '#title' => t('Field test field widget setting'),
    '#default_value' => $settings['test_widget_setting'],
    '#required' => FALSE,
    '#description' => t('A dummy form element to simulate field widget setting.'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
