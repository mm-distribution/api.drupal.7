# DatabaseSelectComplexTestCase::testLeftOuterJoin()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2170–2190 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2170-L2190)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLeftOuterJoin()
```

## Documentation

```text
Test LEFT OUTER joins.
```

## Code

```php
  function testLeftOuterJoin() {
    $query = db_select('test', 'p');
    $people_alias = $query->leftJoin('test_task', 't', 't.pid = p.id');
    $name_field = $query->addField('p', 'name', 'name');
    $task_field = $query->addField($people_alias, 'task', 'task');
    $priority_field = $query->addField($people_alias, 'priority', 'priority');

    $query->orderBy($name_field);
    $result = $query->execute();

    $num_records = 0;
    $last_name = 0;

    foreach ($result as $record) {
      $num_records++;
      $this->assertTrue(strcmp($record->$name_field, $last_name) >= 0, 'Results returned in correct order.');
      $last_priority = $record->$name_field;
    }

    $this->assertEqual($num_records, 8, 'Returned the correct number of rows.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
