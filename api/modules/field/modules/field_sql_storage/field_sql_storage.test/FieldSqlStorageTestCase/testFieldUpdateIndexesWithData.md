# FieldSqlStorageTestCase::testFieldUpdateIndexesWithData()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 432–472 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L432-L472)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldUpdateIndexesWithData()
```

## Documentation

```text
Test adding and removing indexes while data is present.
```

## Code

```php
  function testFieldUpdateIndexesWithData() {

    // Create a decimal field.
    $field_name = 'testfield';
    $field = array('field_name' => $field_name, 'type' => 'text');
    $field = field_create_field($field);
    $instance = array('field_name' => $field_name, 'entity_type' => 'test_entity', 'bundle' => 'test_bundle');
    $instance = field_create_instance($instance);
    $tables = array(_field_sql_storage_tablename($field), _field_sql_storage_revision_tablename($field));

    // Verify the indexes we will create do not exist yet.
    foreach ($tables as $table) {
      $this->assertFalse(Database::getConnection()->schema()->indexExists($table, 'value'), format_string("No index named value exists in %table", array('%table' => $table)));
      $this->assertFalse(Database::getConnection()->schema()->indexExists($table, 'value_format'), format_string("No index named value_format exists in %table", array('%table' => $table)));
    }

    // Add data so the table cannot be dropped.
    $entity = field_test_create_stub_entity(0, 0, $instance['bundle']);
    $entity->{$field_name}[LANGUAGE_NONE][0]['value'] = 'field data';
    field_attach_insert('test_entity', $entity);

    // Add an index
    $field = array('field_name' => $field_name, 'indexes' => array('value' => array(array('value', 255))));
    field_update_field($field);
    foreach ($tables as $table) {
      $this->assertTrue(Database::getConnection()->schema()->indexExists($table, "{$field_name}_value"), format_string("Index on value created in %table", array('%table' => $table)));
    }

    // Add a different index, removing the existing custom one.
    $field = array('field_name' => $field_name, 'indexes' => array('value_format' => array(array('value', 127), array('format', 127))));
    field_update_field($field);
    foreach ($tables as $table) {
      $this->assertTrue(Database::getConnection()->schema()->indexExists($table, "{$field_name}_value_format"), format_string("Index on value_format created in %table", array('%table' => $table)));
      $this->assertFalse(Database::getConnection()->schema()->indexExists($table, "{$field_name}_value"), format_string("Index on value removed in %table", array('%table' => $table)));
    }

    // Verify that the tables were not dropped.
    $entity = field_test_create_stub_entity(0, 0, $instance['bundle']);
    field_attach_load('test_entity', array(0 => $entity));
    $this->assertEqual($entity->{$field_name}[LANGUAGE_NONE][0]['value'], 'field data', "Index changes performed without dropping the tables");
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
