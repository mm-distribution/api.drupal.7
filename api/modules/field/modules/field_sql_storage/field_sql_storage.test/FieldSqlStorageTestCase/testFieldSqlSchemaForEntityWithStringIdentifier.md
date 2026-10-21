# FieldSqlStorageTestCase::testFieldSqlSchemaForEntityWithStringIdentifier()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 116–134 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L116-L134)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldSqlSchemaForEntityWithStringIdentifier()
```

## Documentation

```text
Tests adding a field with an entity ID type of string.
```

## Code

```php
  function testFieldSqlSchemaForEntityWithStringIdentifier() {
    // Test programmatically adding field with string ID.
    $field_name = 'string_id_example';
    $field = array('field_name' => $field_name, 'type' => 'text', 'settings' => array('max_length' => 255), 'entity_id_type' => 'string');
    field_create_field($field);
    $schema = drupal_get_schema('field_data_' . $field_name);

    $this->assertEqual($schema['fields']['entity_id']['type'], 'varchar');
    $this->assertEqual($schema['fields']['revision_id']['type'], 'varchar');

    // Test programmatically adding field with default ID(int).
    $field_name = 'default_id_example';
    $field = array('field_name' => $field_name, 'type' => 'text', 'settings' => array('max_length' => 255));
    field_create_field($field);
    $schema = drupal_get_schema('field_data_' . $field_name);

    $this->assertEqual($schema['fields']['entity_id']['type'], 'int');
    $this->assertEqual($schema['fields']['revision_id']['type'], 'int');
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
