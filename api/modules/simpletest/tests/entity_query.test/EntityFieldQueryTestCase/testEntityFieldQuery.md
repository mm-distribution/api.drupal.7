# EntityFieldQueryTestCase::testEntityFieldQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 168–1078 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L168-L1078)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQuery()
```

## Documentation

```text
Tests EntityFieldQuery.
```

## Code

```php
  function testEntityFieldQuery() {
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle')
      ->entityCondition('entity_id', '5');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle', 5),
    ), 'Test query on an entity type with a generated bundle.');

    // Test entity_type condition.
    $query = new EntityFieldQuery();
    $query->entityCondition('entity_type', 'test_entity_bundle_key');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test entity entity_type condition.');

    // Test entity_id condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityCondition('entity_id', '3');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
    ), 'Test entity entity_id condition.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', '3');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
    ), 'Test entity entity_id condition and entity_id property condition.');

    // Test bundle condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityCondition('bundle', 'bundle1');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test entity bundle condition: bundle1.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityCondition('bundle', 'bundle2');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test entity bundle condition: bundle2.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('fttype', 'bundle2');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test entity bundle condition and bundle property condition.');

    // Test revision_id condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->entityCondition('revision_id', '3');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 3),
    ), 'Test entity revision_id condition.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->propertyCondition('ftvid', '3');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 3),
    ), 'Test entity revision_id condition and revision_id property condition.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->fieldCondition($this->fields[0], 'value', 100, '>=')
      ->age(FIELD_LOAD_REVISION);
    $this->assertEntityFieldQuery($query, array(
        array('test_entity', 100),
        array('test_entity', 101),
    ), 'Test revision age.');

    // Test that fields attached to the non-revision supporting entity
    // 'test_entity_bundle_key' are reachable in FIELD_LOAD_REVISION.
    $query = new EntityFieldQuery();
    $query
      ->fieldCondition($this->fields[0], 'value', 100, '<')
      ->age(FIELD_LOAD_REVISION);
    $this->assertEntityFieldQuery($query, array(
        array('test_entity_bundle_key', 1),
        array('test_entity_bundle_key', 2),
        array('test_entity_bundle_key', 3),
        array('test_entity_bundle_key', 4),
        array('test_entity_bundle_key', 5),
        array('test_entity_bundle_key', 6),
        array('test_entity', 1),
        array('test_entity', 2),
        array('test_entity', 3),
        array('test_entity', 4),
    ), 'Test that fields are reachable from FIELD_LOAD_REVISION even for non-revision entities.');

    // Test entity sort by entity_id.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityOrderBy('entity_id', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test sort entity entity_id in ascending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityOrderBy('entity_id', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test sort entity entity_id in descending order.', TRUE);

    // Test entity sort by entity_id, with a field condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->entityOrderBy('entity_id', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test sort entity entity_id in ascending order, with a field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test sort entity entity_id property in descending order, with a field condition.', TRUE);

    // Test property sort by entity id.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test sort entity entity_id property in ascending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test sort entity entity_id property in descending order.', TRUE);

    // Test property sort by entity id, with a field condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftid', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test sort entity entity_id property in ascending order, with a field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test sort entity entity_id property in descending order, with a field condition.', TRUE);

    // Test entity sort by bundle.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityOrderBy('bundle', 'ASC')
      ->propertyOrderBy('ftid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
    ), 'Test sort entity bundle in ascending order, property in descending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityOrderBy('bundle', 'DESC')
      ->propertyOrderBy('ftid', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test sort entity bundle in descending order, property in ascending order.', TRUE);

    // Test entity sort by bundle, with a field condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->entityOrderBy('bundle', 'ASC')
      ->propertyOrderBy('ftid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
    ), 'Test sort entity bundle in ascending order, property in descending order, with a field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->entityOrderBy('bundle', 'DESC')
      ->propertyOrderBy('ftid', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test sort entity bundle in descending order, property in ascending order, with a field condition.', TRUE);

    // Test entity sort by bundle, field.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityOrderBy('bundle', 'ASC')
      ->fieldOrderBy($this->fields[0], 'value', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
    ), 'Test sort entity bundle in ascending order, field in descending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityOrderBy('bundle', 'DESC')
      ->fieldOrderBy($this->fields[0], 'value', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test sort entity bundle in descending order, field in ascending order.', TRUE);

    // Test entity sort by revision_id.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->entityOrderBy('revision_id', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 3),
      array('test_entity', 4),
    ), 'Test sort entity revision_id in ascending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->entityOrderBy('revision_id', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 4),
      array('test_entity', 3),
      array('test_entity', 2),
      array('test_entity', 1),
    ), 'Test sort entity revision_id in descending order.', TRUE);

    // Test entity sort by revision_id, with a field condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->entityOrderBy('revision_id', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 3),
      array('test_entity', 4),
    ), 'Test sort entity revision_id in ascending order, with a field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->entityOrderBy('revision_id', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 4),
      array('test_entity', 3),
      array('test_entity', 2),
      array('test_entity', 1),
    ), 'Test sort entity revision_id in descending order, with a field condition.', TRUE);

    // Test property sort by revision_id.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->propertyOrderBy('ftvid', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 3),
      array('test_entity', 4),
    ), 'Test sort entity revision_id property in ascending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->propertyOrderBy('ftvid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 4),
      array('test_entity', 3),
      array('test_entity', 2),
      array('test_entity', 1),
    ), 'Test sort entity revision_id property in descending order.', TRUE);

    // Test property sort by revision_id, with a field condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftvid', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 3),
      array('test_entity', 4),
    ), 'Test sort entity revision_id property in ascending order, with a field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftvid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity', 4),
      array('test_entity', 3),
      array('test_entity', 2),
      array('test_entity', 1),
    ), 'Test sort entity revision_id property in descending order, with a field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldOrderBy($this->fields[0], 'value', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test sort field in ascending order without field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldOrderBy($this->fields[0], 'value', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test sort field in descending order without field condition.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->fieldOrderBy($this->fields[0], 'value', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test sort field in ascending order.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->fieldOrderBy($this->fields[0], 'value', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test sort field in descending order.', TRUE);

    // Test "in" operation with entity entity_type condition and entity_id
    // property condition.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', array(1, 3, 4), 'IN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test "in" operation with entity entity_type condition and entity_id property condition.');

    // Test "in" operation with entity entity_type condition and entity_id
    // property condition. Sort in descending order by entity_id.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', array(1, 3, 4), 'IN')
      ->propertyOrderBy('ftid', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 1),
    ), 'Test "in" operation with entity entity_type condition and entity_id property condition. Sort entity_id in descending order.', TRUE);

    // Test query count
    $query = new EntityFieldQuery();
    $query_count = $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->count()
      ->execute();
    $this->assertEqual($query_count, 6, 'Test query count on entity condition.');

    $query = new EntityFieldQuery();
    $query_count = $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', '1')
      ->count()
      ->execute();
    $this->assertEqual($query_count, 1, 'Test query count on entity and property condition.');

    $query = new EntityFieldQuery();
    $query_count = $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', '4', '>')
      ->count()
      ->execute();
    $this->assertEqual($query_count, 2, 'Test query count on entity and property condition with operator.');

    $query = new EntityFieldQuery();
    $query_count = $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 3, '=')
      ->count()
      ->execute();
    $this->assertEqual($query_count, 1, 'Test query count on field condition.');

    // First, test without options.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('fttype', 'und', 'CONTAINS');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "contains" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[1], 'shape', 'uar', 'CONTAINS');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle', 5),
    ), 'Test the "contains" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 1, '=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
    ), 'Test the "equal to" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 3, '=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity', 3),
    ), 'Test the "equal to" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 3, '<>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "not equal to" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 3, '<>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 4),
    ), 'Test the "not equal to" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 3, '!=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "not equal to" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 3, '!=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 4),
    ), 'Test the "not equal to" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 2, '<');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
    ), 'Test the "less than" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 2, '<');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity', 1),
    ), 'Test the "less than" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 2, '<=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
    ), 'Test the "less than or equal to" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 2, '<=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity', 1),
      array('test_entity', 2),
    ), 'Test the "less than or equal to" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 4, '>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "greater than" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 2, '>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity', 3),
      array('test_entity', 4),
    ), 'Test the "greater than" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 4, '>=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "greater than or equal to" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 3, '>=');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity', 3),
      array('test_entity', 4),
    ), 'Test the "greater than or equal to" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', array(3, 4), 'NOT IN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "not in" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', array(3, 4, 100, 101), 'NOT IN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity', 1),
      array('test_entity', 2),
    ), 'Test the "not in" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', array(3, 4), 'IN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test the "in" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', array(2, 3), 'IN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity', 2),
      array('test_entity', 3),
    ), 'Test the "in" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', array(1, 3), 'BETWEEN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
    ), 'Test the "between" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', array(1, 3), 'BETWEEN');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity', 1),
      array('test_entity', 2),
      array('test_entity', 3),
    ), 'Test the "between" operation on a field.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('fttype', 'bun', 'STARTS_WITH');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test the "starts_with" operation on a property.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[1], 'shape', 'squ', 'STARTS_WITH');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle', 5),
    ), 'Test the "starts_with" operation on a field.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 3);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity', 3),
    ), 'Test omission of an operator with a single item.');

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', array(2, 3));
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity', 2),
      array('test_entity', 3),
    ), 'Test omission of an operator with multiple items.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyCondition('ftid', 1, '>')
      ->fieldCondition($this->fields[0], 'value', 4, '<');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
    ), 'Test entity, property and field conditions.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->entityCondition('bundle', 'bundle', 'STARTS_WITH')
      ->propertyCondition('ftid', 4)
      ->fieldCondition($this->fields[0], 'value', 4);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
    ), 'Test entity condition with "starts_with" operation, and property and field conditions.');

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'ASC')
      ->range(0, 2);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
    ), 'Test limit on a property.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>=')
      ->fieldOrderBy($this->fields[0], 'value', 'ASC')
      ->range(0, 2);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
    ), 'Test limit on a field.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'ASC')
      ->range(4, 6);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test offset on a property.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->fieldOrderBy($this->fields[0], 'value', 'ASC')
      ->range(2, 4);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test offset on a field.', TRUE);

    for ($i = 6; $i < 10; $i++) {
      $entity = new stdClass();
      $entity->ftid = $i;
      $entity->fttype = 'test_entity_bundle';
      $entity->{$this->field_names[0]}[LANGUAGE_NONE][0]['value'] = $i - 5;
      drupal_write_record('test_entity_bundle', $entity);
      field_attach_insert('test_entity_bundle', $entity);
    }

    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', 2, '>');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity', 3),
      array('test_entity', 4),
      array('test_entity_bundle', 8),
      array('test_entity_bundle', 9),
    ), 'Select a field across multiple entities.');

    $query = new EntityFieldQuery();
    $query
      ->fieldCondition($this->fields[1], 'shape', 'square')
      ->fieldCondition($this->fields[1], 'color', 'blue');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle', 5),
    ), 'Test without a delta group.');

    $query = new EntityFieldQuery();
    $query
      ->fieldCondition($this->fields[1], 'shape', 'square', '=', 'group')
      ->fieldCondition($this->fields[1], 'color', 'blue', '=', 'group');
    $this->assertEntityFieldQuery($query, array(), 'Test with a delta group.');

    // Test query on a deleted field.
    field_attach_delete_bundle('test_entity_bundle_key', 'bundle1');
    field_attach_delete_bundle('test_entity', 'test_bundle');
    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', '3');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle', 8),
    ), 'Test query on a field after deleting field from some entities.');

    field_attach_delete_bundle('test_entity_bundle', 'test_entity_bundle');
    $query = new EntityFieldQuery();
    $query->fieldCondition($this->fields[0], 'value', '3');
    $this->assertEntityFieldQuery($query, array(), 'Test query on a field after deleting field from all entities.');

    $query = new EntityFieldQuery();
    $query
      ->fieldCondition($this->fields[0], 'value', '3')
      ->deleted(TRUE);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle', 8),
      array('test_entity', 3),
    ), 'Test query on a deleted field with deleted option set to TRUE.');

    $pass = FALSE;
    $query = new EntityFieldQuery();
    try {
      $query->execute();
    }
    catch (EntityFieldQueryException $exception) {
      $pass = ($exception->getMessage() == t('For this query an entity type must be specified.'));
    }
    $this->assertTrue($pass, "Can't query the universe.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
