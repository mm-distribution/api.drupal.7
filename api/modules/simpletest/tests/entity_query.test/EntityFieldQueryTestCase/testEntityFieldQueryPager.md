# EntityFieldQueryTestCase::testEntityFieldQueryPager()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1363–1413 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1363-L1413)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryPager()
```

## Documentation

```text
Tests the pager integration of EntityFieldQuery.
```

## Code

```php
  function testEntityFieldQueryPager() {
    // Test pager in propertyQuery
    $_GET['page'] = '0,1';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'ASC')
      ->pager(3, 0);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
    ), 'Test pager integration in propertyQuery: page 1.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'ASC')
      ->pager(3, 1);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'Test pager integration in propertyQuery: page 2.', TRUE);

    // Test pager in field storage
    $_GET['page'] = '0,1';
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftid', 'ASC')
      ->pager(2, 0);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
    ), 'Test pager integration in field storage: page 1.', TRUE);

    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->fieldCondition($this->fields[0], 'value', 0, '>')
      ->propertyOrderBy('ftid', 'ASC')
      ->pager(2, 1);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
    ), 'Test pager integration in field storage: page 2.', TRUE);

    unset($_GET['page']);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
