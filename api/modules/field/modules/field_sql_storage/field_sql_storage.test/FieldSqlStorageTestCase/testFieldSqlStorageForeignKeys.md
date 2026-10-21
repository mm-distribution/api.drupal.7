# FieldSqlStorageTestCase::testFieldSqlStorageForeignKeys()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 505–536 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L505-L536)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldSqlStorageForeignKeys()
```

## Documentation

```text
Test foreign key support.
```

## Code

```php
  function testFieldSqlStorageForeignKeys() {
    // Create a 'shape' field, with a configurable foreign key (see
    // field_test_field_schema()).
    $field_name = 'testfield';
    $foreign_key_name = 'shape';
    $field = array('field_name' => $field_name, 'type' => 'shape', 'settings' => array('foreign_key_name' => $foreign_key_name));
    field_create_field($field);

    // Retrieve the field definition and check that the foreign key is in place.
    $field = field_info_field($field_name);
    $this->assertEqual($field['foreign keys'][$foreign_key_name]['table'], $foreign_key_name, 'Foreign key table name preserved through CRUD');
    $this->assertEqual($field['foreign keys'][$foreign_key_name]['columns'][$foreign_key_name], 'id', 'Foreign key column name preserved through CRUD');

    // Update the field settings, it should update the foreign key definition
    // too.
    $foreign_key_name = 'color';
    $field['settings']['foreign_key_name'] = $foreign_key_name;
    field_update_field($field);

    // Retrieve the field definition and check that the foreign key is in place.
    $field = field_info_field($field_name);
    $this->assertEqual($field['foreign keys'][$foreign_key_name]['table'], $foreign_key_name, 'Foreign key table name modified after update');
    $this->assertEqual($field['foreign keys'][$foreign_key_name]['columns'][$foreign_key_name], 'id', 'Foreign key column name modified after update');

    // Now grab the SQL schema and verify that too.
    $schema = drupal_get_schema(_field_sql_storage_tablename($field), TRUE);
    $this->assertEqual(count($schema['foreign keys']), 1, 'There is 1 foreign key in the schema');
    $foreign_key = reset($schema['foreign keys']);
    $foreign_key_column = _field_sql_storage_columnname($field['field_name'], $foreign_key_name);
    $this->assertEqual($foreign_key['table'], $foreign_key_name, 'Foreign key table name preserved in the schema');
    $this->assertEqual($foreign_key['columns'][$foreign_key_column], 'id', 'Foreign key column name preserved in the schema');
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
