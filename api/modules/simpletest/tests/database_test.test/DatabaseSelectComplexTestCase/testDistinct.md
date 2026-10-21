# DatabaseSelectComplexTestCase::testDistinct()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2283–2295 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2283-L2295)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDistinct()
```

## Documentation

```text
Test distinct queries.
```

## Code

```php
  function testDistinct() {
    $query = db_select('test_task');
    $task_field = $query->addField('test_task', 'task');
    $query->distinct();
    $result = $query->execute();

    $num_records = 0;
    foreach ($result as $record) {
      $num_records++;
    }

    $this->assertEqual($num_records, 6, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
