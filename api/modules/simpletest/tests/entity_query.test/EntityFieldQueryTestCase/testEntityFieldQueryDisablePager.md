# EntityFieldQueryTestCase::testEntityFieldQueryDisablePager()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1418–1434 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1418-L1434)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryDisablePager()
```

## Documentation

```text
Tests disabling the pager in EntityFieldQuery.
```

## Code

```php
  function testEntityFieldQueryDisablePager() {
    // Test enabling a pager and then disabling it.
    $query = new EntityFieldQuery();
    $query
      ->entityCondition('entity_type', 'test_entity_bundle_key')
      ->propertyOrderBy('ftid', 'ASC')
      ->pager(1)
      ->pager(0);
    $this->assertEntityFieldQuery($query, array(
      array('test_entity_bundle_key', 1),
      array('test_entity_bundle_key', 2),
      array('test_entity_bundle_key', 3),
      array('test_entity_bundle_key', 4),
      array('test_entity_bundle_key', 5),
      array('test_entity_bundle_key', 6),
    ), 'All test entities are listed when the pager is enabled and then disabled.', TRUE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
