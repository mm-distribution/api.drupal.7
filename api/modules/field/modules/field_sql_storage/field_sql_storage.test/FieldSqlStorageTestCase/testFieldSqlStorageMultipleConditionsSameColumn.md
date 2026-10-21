# FieldSqlStorageTestCase::testFieldSqlStorageMultipleConditionsSameColumn()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 543–577 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L543-L577)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
function testFieldSqlStorageMultipleConditionsSameColumn()
```

## Documentation

```text
Test handling multiple conditions on one column of a field.

Tests both the result and the complexity of the query.
```

## Code

```php
  function testFieldSqlStorageMultipleConditionsSameColumn() {
    $entity = field_test_create_stub_entity(NULL, NULL);
    $entity->{$this->field_name}[LANGUAGE_NONE][0] = array('value' => 1);
    field_test_entity_save($entity);

    $entity = field_test_create_stub_entity(NULL, NULL);
    $entity->{$this->field_name}[LANGUAGE_NONE][0] = array('value' => 2);
    field_test_entity_save($entity);

    $entity = field_test_create_stub_entity(NULL, NULL);
    $entity->{$this->field_name}[LANGUAGE_NONE][0] = array('value' => 3);
    field_test_entity_save($entity);

    $query = new EntityFieldQuery();
    // This tag causes field_test_query_store_global_test_query_alter() to be
    // invoked so that the query can be tested.
    $query->addTag('store_global_test_query');
    $query->entityCondition('entity_type', 'test_entity');
    $query->entityCondition('bundle', 'test_bundle');
    $query->fieldCondition($this->field_name, 'value', 1, '<>', 0, LANGUAGE_NONE);
    $query->fieldCondition($this->field_name, 'value', 2, '<>', 0, LANGUAGE_NONE);
    $result = field_sql_storage_field_storage_query($query);

    // Test the results.
    $this->assertEqual(1, count($result), format_string('One result should be returned, got @count', array('@count' => count($result))));

    // Test the complexity of the query.
    $query = $GLOBALS['test_query'];
    $this->assertNotNull($query, 'Precondition: the query should be available');
    $tables = $query->getTables();
    $this->assertEqual(1, count($tables), 'The query contains just one table.');

    // Clean up.
    unset($GLOBALS['test_query']);
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
