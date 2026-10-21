# EntityFieldQueryTestCase::testEntityFieldQueryTableSort()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1439–1611 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1439-L1611)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryTableSort()
```

## Documentation

```text
Tests the TableSort integration of EntityFieldQuery.
```

## Code

```php
  function testEntityFieldQueryTableSort() {
    // Test TableSort in propertyQuery
    $_GET['sort'] = 'asc';
    $_GET['order'] = 'Id';
    $header = array(
      'id' => array('data' => 'Id', 'type' => 'property',  'specifier' => 'ftid'),
      'type' => array('data' => 'Type', 'type' => 'entity', 'specifier' => 'bundle'),
    );
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test TableSort by property: ftid ASC in propertyQuery.', TRUE);

    $_GET['sort'] = 'desc';
    $_GET['order'] = 'Id';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test TableSort by property: ftid DESC in propertyQuery.', TRUE);

    $_GET['sort'] = 'asc';
    $_GET['order'] = 'Type';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test TableSort by entity: bundle ASC in propertyQuery.', TRUE);

    $_GET['sort'] = 'desc';
    $_GET['order'] = 'Type';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test TableSort by entity: bundle DESC in propertyQuery.', TRUE);

    // Test TableSort in field storage
    $_GET['sort'] = 'asc';
    $_GET['order'] = 'Id';
    $header = array(
      'id' => array('data' => 'Id', 'type' => 'property',  'specifier' => 'ftid'),
      'type' => array('data' => 'Type', 'type' => 'entity', 'specifier' => 'bundle'),
      'field' => array('data' => 'Field', 'type' => 'field', 'specifier' => array('field' => $this->field_names[0], 'column' => 'value')),
    );
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test TableSort by property: ftid ASC in field storage.', TRUE);

    $_GET['sort'] = 'desc';
    $_GET['order'] = 'Id';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test TableSort by property: ftid DESC in field storage.', TRUE);

    $_GET['sort'] = 'asc';
    $_GET['order'] = 'Type';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->tableSort($header)
      ->entityOrderBy('entity_id', 'DESC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
    ), 'Test TableSort by entity: bundle ASC in field storage.', TRUE);

    $_GET['sort'] = 'desc';
    $_GET['order'] = 'Type';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->tableSort($header)
      ->entityOrderBy('entity_id', 'ASC');
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test TableSort by entity: bundle DESC in field storage.', TRUE);

    $_GET['sort'] = 'asc';
    $_GET['order'] = 'Field';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test TableSort by field ASC.', TRUE);

    $_GET['sort'] = 'desc';
    $_GET['order'] = 'Field';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->tableSort($header);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 6),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 1),
    ), 'Test TableSort by field DESC.', TRUE);

    unset($_GET['sort']);
    unset($_GET['order']);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
