# field_test_field_widget_info()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 168–184 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L168-L184)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_info()](../../field.api.php/hook_field_widget_info.md)

## Signature

```php
function field_test_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().
```

## Code

```php
function field_test_field_widget_info() {
  return array(
    'test_field_widget' => array(
      'label' => t('Test field'),
      'field types' => array('test_field', 'hidden_test_field'),
      'settings' => array('test_widget_setting' => 'dummy test string'),
    ),
    'test_field_widget_multiple' => array(
      'label' => t('Test field 1'),
      'field types' => array('test_field'),
      'settings' => array('test_widget_setting_multiple' => 'dummy test string'),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
