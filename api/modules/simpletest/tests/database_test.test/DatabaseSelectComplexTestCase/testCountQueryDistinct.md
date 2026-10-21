# DatabaseSelectComplexTestCase::testCountQueryDistinct()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2378–2386 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2378-L2386)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCountQueryDistinct()
```

## Documentation

```text
Test that we can generate a count query from a query with distinct.
```

## Code

```php
  function testCountQueryDistinct() {
    $query = db_select('test_task');
    $task_field = $query->addField('test_task', 'task');
    $query->distinct();

    $count = $query->countQuery()->execute()->fetchField();

    $this->assertEqual($count, 6, 'Counted the correct number of records.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
