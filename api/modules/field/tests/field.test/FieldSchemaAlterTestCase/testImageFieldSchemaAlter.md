# FieldSchemaAlterTestCase::testImageFieldSchemaAlter()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 2898–2917 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L2898-L2917)
- **Class:** [FieldSchemaAlterTestCase](../FieldSchemaAlterTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testImageFieldSchemaAlter()
```

## Documentation

```text
Tests a hook_field_schema_alter() implementation.

@see field_test_schema_alter_field_schema_alter()
```

## Code

```php
  function testImageFieldSchemaAlter() {
    $test_field = array(
      'field_name' => drupal_strtolower($this->randomName()),
      'type' => 'test_field',
    );
    field_create_field($test_field);
    $test_field_name = $test_field['field_name'];
    $test_field_instance_settings = array(
      'field_name' => $test_field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'deleted' => 0,
    );
    $test_field_instance = field_create_instance($test_field_instance_settings);

    $table_name = _field_sql_storage_tablename($test_field_instance);
    $schema = drupal_get_schema($table_name, TRUE);
    $this->assertEqual('float', $schema['fields'][$test_field_name .'_value']['type']);
    $this->assertTrue(db_field_exists($table_name, $test_field_name .'_additional_column'));
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
