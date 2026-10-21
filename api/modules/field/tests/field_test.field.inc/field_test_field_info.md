# field_test_field_info()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 11–48 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L11-L48)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_info()](../../field.api.php/hook_field_info.md)

## Signature

```php
function field_test_field_info()
```

## Documentation

```text
Implements hook_field_info().
```

## Code

```php
function field_test_field_info() {
  return array(
    'test_field' => array(
      'label' => t('Test field'),
      'description' => t('Dummy field type used for tests.'),
      'settings' => array(
        'test_field_setting' => 'dummy test string',
        'changeable' => 'a changeable field setting',
        'unchangeable' => 'an unchangeable field setting',
      ),
      'instance_settings' => array(
        'test_instance_setting' => 'dummy test string',
        'test_hook_field_load' => FALSE,
      ),
      'default_widget' => 'test_field_widget',
      'default_formatter' => 'field_test_default',
    ),
    'shape' => array(
      'label' => t('Shape'),
      'description' => t('Another dummy field type.'),
      'settings' => array(
        'foreign_key_name' => 'shape',
      ),
      'instance_settings' => array(),
      'default_widget' => 'test_field_widget',
      'default_formatter' => 'field_test_default',
    ),
    'hidden_test_field' => array(
      'no_ui' => TRUE,
      'label' => t('Hidden from UI test field'),
      'description' => t('Dummy hidden field type used for tests.'),
      'settings' => array(),
      'instance_settings' => array(),
      'default_widget' => 'test_field_widget',
      'default_formatter' => 'field_test_default',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
