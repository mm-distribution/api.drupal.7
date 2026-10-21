# DatabaseSelectComplexTestCase::testDefaultJoin()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2145–2165 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2145-L2165)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDefaultJoin()
```

## Documentation

```text
Test simple JOIN statements.
```

## Code

```php
  function testDefaultJoin() {
    $query = db_select('test_task', 't');
    $people_alias = $query->join('test', 'p', 't.pid = p.id');
    $name_field = $query->addField($people_alias, 'name', 'name');
    $task_field = $query->addField('t', 'task', 'task');
    $priority_field = $query->addField('t', 'priority', 'priority');

    $query->orderBy($priority_field);
    $result = $query->execute();

    $num_records = 0;
    $last_priority = 0;
    foreach ($result as $record) {
      $num_records++;
      $this->assertTrue($record->$priority_field >= $last_priority, 'Results returned in correct order.');
      $this->assertNotEqual($record->$name_field, 'Ringo', 'Taskless person not selected.');
      $last_priority = $record->$priority_field;
    }

    $this->assertEqual($num_records, 7, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
