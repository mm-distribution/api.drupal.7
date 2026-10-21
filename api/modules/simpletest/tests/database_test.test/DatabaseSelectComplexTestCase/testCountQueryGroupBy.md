# DatabaseSelectComplexTestCase::testCountQueryGroupBy()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2391–2411 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2391-L2411)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCountQueryGroupBy()
```

## Documentation

```text
Test that we can generate a count query from a query with GROUP BY.
```

## Code

```php
  function testCountQueryGroupBy() {
    $query = db_select('test_task');
    $pid_field = $query->addField('test_task', 'pid');
    $query->groupBy('pid');

    $count = $query->countQuery()->execute()->fetchField();

    $this->assertEqual($count, 3, 'Counted the correct number of records.');

    // Use a column alias as, without one, the query can succeed for the wrong
    // reason.
    $query = db_select('test_task');
    $pid_field = $query->addField('test_task', 'pid', 'pid_alias');
    $query->addExpression('COUNT(test_task.task)', 'count');
    $query->groupBy('pid_alias');
    $query->orderBy('pid_alias', 'asc');

    $count = $query->countQuery()->execute()->fetchField();

    $this->assertEqual($count, 3, 'Counted the correct number of records.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
