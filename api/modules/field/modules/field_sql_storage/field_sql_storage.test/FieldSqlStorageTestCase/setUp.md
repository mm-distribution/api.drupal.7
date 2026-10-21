# FieldSqlStorageTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 29–43 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L29-L43)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('field_sql_storage', 'field', 'field_test', 'text');
    $this->field_name = strtolower($this->randomName());
    $this->field = array('field_name' => $this->field_name, 'type' => 'test_field', 'cardinality' => 4);
    $this->field = field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle'
    );
    $this->instance = field_create_instance($this->instance);
    $this->table = _field_sql_storage_tablename($this->field);
    $this->revision_table = _field_sql_storage_revision_tablename($this->field);

  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
