# DatabaseDeleteTruncateTestCase::testSubselectDelete()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1166–1182 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1166-L1182)
- **Class:** [DatabaseDeleteTruncateTestCase](../DatabaseDeleteTruncateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSubselectDelete()
```

## Documentation

```text
Confirm that we can use a subselect in a delete successfully.
```

## Code

```php
  function testSubselectDelete() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_task}')->fetchField();
    $pid_to_delete = db_query("SELECT * FROM {test_task} WHERE task = 'sleep'")->fetchField();

    $subquery = db_select('test', 't')
      ->fields('t', array('id'))
      ->condition('t.id', array($pid_to_delete), 'IN');
    $delete = db_delete('test_task')
      ->condition('task', 'sleep')
      ->condition('pid', $subquery, 'IN');

    $num_deleted = $delete->execute();
    $this->assertEqual($num_deleted, 1, "Deleted 1 record.");

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_task}')->fetchField();
    $this->assertEqual($num_records_before, $num_records_after + $num_deleted, 'Deletion adds up.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
