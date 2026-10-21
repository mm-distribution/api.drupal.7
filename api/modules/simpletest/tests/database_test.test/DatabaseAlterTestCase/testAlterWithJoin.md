# DatabaseAlterTestCase::testAlterWithJoin()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2954–2973 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2954-L2973)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlterWithJoin()
```

## Documentation

```text
Test that we can alter the joins on a query.
```

## Code

```php
  function testAlterWithJoin() {
    $query = db_select('test_task');
    $tid_field = $query->addField('test_task', 'tid');
    $task_field = $query->addField('test_task', 'task');
    $query->orderBy($task_field);
    $query->addTag('database_test_alter_add_join');

    $result = $query->execute();

    $records = $result->fetchAll();

    $this->assertEqual(count($records), 2, 'Returned the correct number of rows.');

    $this->assertEqual($records[0]->name, 'George', 'Correct data retrieved.');
    $this->assertEqual($records[0]->$tid_field, 4, 'Correct data retrieved.');
    $this->assertEqual($records[0]->$task_field, 'sing', 'Correct data retrieved.');
    $this->assertEqual($records[1]->name, 'George', 'Correct data retrieved.');
    $this->assertEqual($records[1]->$tid_field, 5, 'Correct data retrieved.');
    $this->assertEqual($records[1]->$task_field, 'sleep', 'Correct data retrieved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
