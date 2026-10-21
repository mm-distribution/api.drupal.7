# DatabaseSelectComplexTestCase::testJoinConditionObject()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 2447–2488 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L2447-L2488)
- **Class:** [DatabaseSelectComplexTestCase](../DatabaseSelectComplexTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testJoinConditionObject()
```

## Documentation

```text
Test that join conditions can use Condition objects.
```

## Code

```php
  function testJoinConditionObject() {
    // Same test as testDefaultJoin, but with a Condition object.
    $query = db_select('test_task', 't');
    $join_cond = db_and()->where('t.pid = p.id');
    $people_alias = $query->join('test', 'p', $join_cond);
    $name_field = $query->addField($people_alias, 'name', 'name');
    $query->addField('t', 'task', 'task');
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

    // Test a condition object that creates placeholders.
    $t1_name = 'John';
    $t2_name = 'George';
    $join_cond = db_and()
      ->condition('t1.name', $t1_name)
      ->condition('t2.name', $t2_name);
    $query = db_select('test', 't1');
    $query->innerJoin('test', 't2', $join_cond);
    $query->addField('t1', 'name', 't1_name');
    $query->addField('t2', 'name', 't2_name');

    $num_records = $query->countQuery()->execute()->fetchField();
    $this->assertEqual($num_records, 1, 'Query expected to return 1 row. Actual: ' . $num_records);
    if ($num_records == 1) {
      $record = $query->execute()->fetchObject();
      $this->assertEqual($record->t1_name, $t1_name, 'Query expected to retrieve name ' . $t1_name . ' from table t1. Actual: ' . $record->t1_name);
      $this->assertEqual($record->t2_name, $t2_name, 'Query expected to retrieve name ' . $t2_name . ' from table t2. Actual: ' . $record->t2_name);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
