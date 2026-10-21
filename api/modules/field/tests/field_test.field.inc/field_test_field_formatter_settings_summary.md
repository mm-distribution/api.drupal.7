# field_test_field_formatter_settings_summary()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 325–344 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L325-L344)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_formatter_settings_summary()](../../../field_ui/field_ui.api.php/hook_field_formatter_settings_summary.md)

## Signature

```php
function field_test_field_formatter_settings_summary($field, $instance, $view_mode)
```

## Documentation

```text
Implements hook_field_formatter_settings_summary().
```

## Code

```php
function field_test_field_formatter_settings_summary($field, $instance, $view_mode) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $summary = '';

  // The name of the setting depends on the formatter type.
  $map = array(
    'field_test_default' => 'test_formatter_setting',
    'field_test_multiple' => 'test_formatter_setting_multiple',
    'field_test_with_prepare_view' => 'test_formatter_setting_additional',
  );

  if (isset($map[$display['type']])) {
    $name = $map[$display['type']];
    $summary = t('@setting: @value', array('@setting' => $name, '@value' => $settings[$name]));
  }

  return $summary;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
