# DatabaseSelectComplexTestCase::testGroupBy()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2195–2226 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2195-L2226)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testGroupBy()
```

## Documentation

```text
Test GROUP BY clauses.
```

## Code

```php
  function testGroupBy() {
    $query = db_select('test_task', 't');
    $count_field = $query->addExpression('COUNT(task)', 'num');
    $task_field = $query->addField('t', 'task');
    $query->orderBy($count_field);
    $query->groupBy($task_field);
    $result = $query->execute();

    $num_records = 0;
    $last_count = 0;
    $records = array();
    foreach ($result as $record) {
      $num_records++;
      $this->assertTrue($record->$count_field >= $last_count, 'Results returned in correct order.');
      $last_count = $record->$count_field;
      $records[$record->$task_field] = $record->$count_field;
    }

    $correct_results = array(
      'eat' => 1,
      'sleep' => 2,
      'code' => 1,
      'found new band' => 1,
      'perform at superbowl' => 1,
    );

    foreach ($correct_results as $task => $count) {
      $this->assertEqual($records[$task], $count, format_string("Correct number of '@task' records found.", array('@task' => $task)));
    }

    $this->assertEqual($num_records, 6, 'Returned the correct number of total rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
