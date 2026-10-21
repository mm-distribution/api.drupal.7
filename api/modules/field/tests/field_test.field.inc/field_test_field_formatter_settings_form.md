# field_test_field_formatter_settings_form()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 294–320 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L294-L320)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_formatter_settings_form()](../../../field_ui/field_ui.api.php/hook_field_formatter_settings_form.md)

## Signature

```php
function field_test_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_formatter_settings_form().
```

## Code

```php
function field_test_field_formatter_settings_form($field, $instance, $view_mode, $form, &$form_state) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $element = array();

  // The name of the setting depends on the formatter type.
  $map = array(
    'field_test_default' => 'test_formatter_setting',
    'field_test_multiple' => 'test_formatter_setting_multiple',
    'field_test_with_prepare_view' => 'test_formatter_setting_additional',
  );

  if (isset($map[$display['type']])) {
    $name = $map[$display['type']];

    $element[$name] = array(
      '#title' => t('Setting'),
      '#type' => 'textfield',
      '#size' => 20,
      '#default_value' => $settings[$name],
      '#required' => TRUE,
    );
  }

  return $element;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
