# DatabaseAlterTestCase::testAlterChangeConditional()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2978–2998 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2978-L2998)
- **Class:** [DatabaseAlterTestCase](../DatabaseAlterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlterChangeConditional()
```

## Documentation

```text
Test that we can alter a query's conditionals.
```

## Code

```php
  function testAlterChangeConditional() {
    $query = db_select('test_task');
    $tid_field = $query->addField('test_task', 'tid');
    $pid_field = $query->addField('test_task', 'pid');
    $task_field = $query->addField('test_task', 'task');
    $people_alias = $query->join('test', 'people', "test_task.pid = people.id");
    $name_field = $query->addField($people_alias, 'name', 'name');
    $query->condition('test_task.tid', '1');
    $query->orderBy($tid_field);
    $query->addTag('database_test_alter_change_conditional');

    $result = $query->execute();

    $records = $result->fetchAll();

    $this->assertEqual(count($records), 1, 'Returned the correct number of rows.');
    $this->assertEqual($records[0]->$name_field, 'John', 'Correct data retrieved.');
    $this->assertEqual($records[0]->$tid_field, 2, 'Correct data retrieved.');
    $this->assertEqual($records[0]->$pid_field, 1, 'Correct data retrieved.');
    $this->assertEqual($records[0]->$task_field, 'sleep', 'Correct data retrieved.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
