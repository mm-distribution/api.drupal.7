# field_test_field_storage_create_field()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 265–278 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L265-L278)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_create_field()](../../field.api.php/hook_field_storage_create_field.md)

## Signature

```php
function field_test_field_storage_create_field($field)
```

## Documentation

```text
Implements hook_field_storage_create_field().
```

## Code

```php
function field_test_field_storage_create_field($field) {
  if ($field['storage']['type'] == 'field_test_storage_failure') {
    throw new Exception('field_test_storage_failure engine always fails to create fields');
  }

  $data = _field_test_storage_data();

  $data[$field['id']] = array(
    'current' => array(),
    'revisions' => array(),
  );

  _field_test_storage_data($data);
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
