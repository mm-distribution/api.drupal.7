# field_test_field_storage_details_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.storage.inc`](_file.md), lines 49–66 · [local source](../../../../../source/modules/field/tests/field_test.storage.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc#L49-L66)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_storage_details_alter()](../../field.api.php/hook_field_storage_details_alter.md)

## Signature

```php
function field_test_field_storage_details_alter(&$details, $field)
```

## Documentation

```text
Implements hook_field_storage_details_alter().

@see FieldAttachStorageTestCase::testFieldStorageDetailsAlter()
```

## Code

```php
function field_test_field_storage_details_alter(&$details, $field) {

  // For testing, storage details are changed only because of the field name.
  if ($field['field_name'] == 'field_test_change_my_details') {
    $columns = array();
    foreach ((array) $field['columns'] as $column_name => $attributes) {
      $columns[$column_name] = $column_name;
    }
    $details['drupal_variables'] = array(
      FIELD_LOAD_CURRENT => array(
        'moon' => $columns,
      ),
      FIELD_LOAD_REVISION => array(
        'mars' => $columns,
      ),
    );
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.storage.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.storage.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
