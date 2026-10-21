# FieldAttachStorageTestCase::testFieldHasData()

- **Type:** Method
- **File:** [`modules/field/tests/field.test`](../_file.md), lines 499–554 · [local source](../../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L499-L554)
- **Class:** [FieldAttachStorageTestCase](../FieldAttachStorageTestCase.md)
- **Module/theme:** field_test_schema_alter

## Signature

```php
function testFieldHasData()
```

## Documentation

```text
Test field_has_data().
```

## Code

```php
  function testFieldHasData() {
    $entity_type = 'test_entity';
    $langcode = LANGUAGE_NONE;

    $field_name = 'field_1';
    $field = array('field_name' => $field_name, 'type' => 'test_field');
    $field = field_create_field($field);

    $this->assertFalse(field_has_data($field), "No data should be detected.");

    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle'
    );
    $instance = field_create_instance($instance);
    $table = _field_sql_storage_tablename($field);
    $revision_table = _field_sql_storage_revision_tablename($field);

    $columns = array('entity_type', 'entity_id', 'revision_id', 'delta', 'language', $field_name . '_value');

    $eid = 0;

    // Insert values into the field revision table.
    $query = db_insert($revision_table)->fields($columns);
    $query->values(array($entity_type, $eid, 0, 0, $langcode, 1));
    $query->execute();

    $this->assertTrue(field_has_data($field), "Revision data only should be detected.");

    $field_name = 'field_2';
    $field = array('field_name' => $field_name, 'type' => 'test_field');
    $field = field_create_field($field);

    $this->assertFalse(field_has_data($field), "No data should be detected.");

    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle'
    );
    $instance = field_create_instance($instance);
    $table = _field_sql_storage_tablename($field);
    $revision_table = _field_sql_storage_revision_tablename($field);

    $columns = array('entity_type', 'entity_id', 'revision_id', 'delta', 'language', $field_name . '_value');

    $eid = 1;

    // Insert values into the field table.
    $query = db_insert($table)->fields($columns);
    $query->values(array($entity_type, $eid, 0, 0, $langcode, 1));
    $query->execute();

    $this->assertTrue(field_has_data($field), "Values only in field table should be detected.");
  }
```

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
