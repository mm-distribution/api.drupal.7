# field_test_field_storage_info()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 12–23 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L12-L23)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_info()](../../field.api.php/hook_field_storage_info.md)

## Signature

```php
function field_test_field_storage_info()
```

## Documentation

```text
Implements hook_field_storage_info().
```

## Code

```php
function field_test_field_storage_info() {
  return array(
    'field_test_storage' => array(
      'label' => t('Test storage'),
      'description' => t('Dummy test storage backend. Stores field values in the variable table.'),
    ),
    'field_test_storage_failure' => array(
      'label' => t('Test storage failure'),
      'description' => t('Dummy test storage backend. Always fails to create fields.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
