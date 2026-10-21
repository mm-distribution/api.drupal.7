# EntityFieldQueryTestCase::testTablePrefixing()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1672–1683 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1672-L1683)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTablePrefixing()
```

## Documentation

```text
Tests EFQ table prefixing with multiple conditions and an altered join.

@see field_test_query_efq_table_prefixing_test_alter()
```

## Code

```php
  function testTablePrefixing() {
    $query = new EntityFieldQuery();
    $query = $query
      ->entityCondition('entity_type', 'test_entity')
      ->entityCondition('bundle', 'test_bundle')
      ->entityCondition('entity_id', '1')
      ->addTag('efq_table_prefixing_test');

    $expected = array(array('test_entity', 1));

    $this->assertEntityFieldQuery($query, $expected, 'An EntityFieldQuery returns the expected results when altered with an additional join on the base table.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
