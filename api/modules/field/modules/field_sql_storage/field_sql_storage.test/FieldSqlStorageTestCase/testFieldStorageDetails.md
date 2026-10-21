# FieldSqlStorageTestCase::testFieldStorageDetails()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 477–500 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L477-L500)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldStorageDetails()
```

## Documentation

```text
Test the storage details.
```

## Code

```php
  function testFieldStorageDetails() {
    $current = _field_sql_storage_tablename($this->field);
    $revision = _field_sql_storage_revision_tablename($this->field);

    // Retrieve the field and instance with field_info so the storage details are attached.
    $field = field_info_field($this->field['field_name']);
    $instance = field_info_instance($this->instance['entity_type'], $this->instance['field_name'], $this->instance['bundle']);

    // The storage details are indexed by a storage engine type.
    $this->assertTrue(array_key_exists('sql', $field['storage']['details']), 'The storage type is SQL.');

    // The SQL details are indexed by table name.
    $details = $field['storage']['details']['sql'];
    $this->assertTrue(array_key_exists($current, $details[FIELD_LOAD_CURRENT]), 'Table name is available in the instance array.');
    $this->assertTrue(array_key_exists($revision, $details[FIELD_LOAD_REVISION]), 'Revision table name is available in the instance array.');

    // Test current and revision storage details together because the columns
    // are the same.
    foreach ((array) $this->field['columns'] as $column_name => $attributes) {
      $storage_column_name = _field_sql_storage_columnname($this->field['field_name'], $column_name);
      $this->assertEqual($details[FIELD_LOAD_CURRENT][$current][$column_name], $storage_column_name, format_string('Column name %value matches the definition in %bin.', array('%value' => $column_name, '%bin' => $current)));
      $this->assertEqual($details[FIELD_LOAD_REVISION][$revision][$column_name], $storage_column_name, format_string('Column name %value matches the definition in %bin.', array('%value' => $column_name, '%bin' => $revision)));
    }
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
