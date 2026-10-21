# EntityFieldQueryTestCase::testEntityFieldQueryRouting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1308–1358 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1308-L1358)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryRouting()
```

## Documentation

```text
Tests the routing feature of EntityFieldQuery.
```

## Code

```php
  function testEntityFieldQueryRouting() {
    // Entity-only query.
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'test_entity_bundle_key');
    $this->assertIdentical($query->queryCallback(), array($query, 'propertyQuery'), 'Entity-only queries are handled by the propertyQuery handler.');

    // Field-only query.
    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', '3');
    $this->assertIdentical($query->queryCallback(), 'field_sql_storage_field_storage_query', 'Pure field queries are handled by the Field storage handler.');

    // Mixed entity and field query.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', '3');
    $this->assertIdentical($query->queryCallback(), 'field_sql_storage_field_storage_query', 'Mixed queries are handled by the Field storage handler.');

    // Overriding with $query->executeCallback.
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'test_entity_bundle_key');
    $query->executeCallback = 'field_test_dummy_field_storage_query';
    $this->assertEntityFieldQuery($query, array(
      array('user', 1),
    ), 'executeCallback can override the query handler.');

    // Overriding with $query->executeCallback via hook_entity_query_alter().
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'test_entity_bundle_key');
    // Add a flag that will be caught by field_test_entity_query_alter().
    variable_set('field_test_entity_query_alter_execute_callback', TRUE);
    $this->assertEntityFieldQuery($query, array(
      array('user', 1),
    ), 'executeCallback can override the query handler when set in a hook_entity_query_alter().');
    variable_set('field_test_entity_query_alter_execute_callback', FALSE);

    // Mixed-storage queries.
    $query = new EntityFieldQuery();
    $query
      ->fieldCondition($this->fields[0], 'value', '3')
      ->fieldCondition($this->fields[1], 'shape', 'squ', 'STARTS_WITH');
    // Alter the storage of the field.
    $query->fields[1]['storage']['module'] = 'dummy_storage';
    try {
      $query->queryCallback();
    }
    catch (EntityFieldQueryException $exception) {
      $pass = ($exception->getMessage() == t("Can't handle more than one field storage engine"));
    }
    $this->assertTrue($pass, 'Cannot query across field storage engines.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
