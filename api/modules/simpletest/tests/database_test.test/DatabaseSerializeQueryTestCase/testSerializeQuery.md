# DatabaseSerializeQueryTestCase::testSerializeQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3276–3285 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3276-L3285)
- **Class:** [DatabaseSerializeQueryTestCase](../DatabaseSerializeQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSerializeQuery()
```

## Documentation

```text
Confirm that a query can be serialized and unserialized.
```

## Code

```php
  function testSerializeQuery() {
    $query = db_select('test');
    $query->addField('test', 'age');
    $query->condition('name', 'Ringo');
    // If this doesn't work, it will throw an exception, so no need for an
    // assertion.
    $query = unserialize(serialize($query));
    $results = $query->execute()->fetchCol();
    $this->assertEqual($results[0], 28, 'Query properly executed after unserialization.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
