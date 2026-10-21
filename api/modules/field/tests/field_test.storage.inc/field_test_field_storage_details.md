# field_test_field_storage_details()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 28–42 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L28-L42)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_details()](../../field.api.php/hook_field_storage_details.md)

## Signature

```php
function field_test_field_storage_details($field)
```

## Documentation

```text
Implements hook_field_storage_details().
```

## Code

```php
function field_test_field_storage_details($field) {
  $details = array();

  // Add field columns.
  $columns = array();
  foreach ((array) $field['columns'] as $column_name => $attributes) {
    $columns[$column_name] = $column_name;
  }
  return array(
    'drupal_variables' => array(
      'field_test_storage_data[FIELD_LOAD_CURRENT]' => $columns,
      'field_test_storage_data[FIELD_LOAD_REVISION]' => $columns,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
