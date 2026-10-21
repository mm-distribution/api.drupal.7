# field_test_field_formatter_info()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.field.inc`](_file.md), lines 263–289 · [local source](../../../../../source/modules/field/tests/field_test.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc#L263-L289)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_formatter_info()](../../field.api.php/hook_field_formatter_info.md)

## Signature

```php
function field_test_field_formatter_info()
```

## Documentation

```text
Implements hook_field_formatter_info().
```

## Code

```php
function field_test_field_formatter_info() {
  return array(
    'field_test_default' => array(
      'label' => t('Default'),
      'description' => t('Default formatter'),
      'field types' => array('test_field'),
      'settings' => array(
        'test_formatter_setting' => 'dummy test string',
      ),
    ),
    'field_test_multiple' => array(
      'label' => t('Multiple'),
      'description' => t('Multiple formatter'),
      'field types' => array('test_field'),
      'settings' => array(
        'test_formatter_setting_multiple' => 'dummy test string',
      ),
    ),
    'field_test_with_prepare_view' => array(
      'label' => t('Tests hook_field_formatter_prepare_view()'),
      'field types' => array('test_field'),
      'settings' => array(
        'test_formatter_setting_additional' => 'dummy test string',
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
