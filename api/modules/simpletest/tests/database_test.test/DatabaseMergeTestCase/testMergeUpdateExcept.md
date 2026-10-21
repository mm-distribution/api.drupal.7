# DatabaseMergeTestCase::testMergeUpdateExcept()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1278–1294 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1278-L1294)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeUpdateExcept()
```

## Documentation

```text
Confirm that we can merge-update a record successfully, with different insert and update.
```

## Code

```php
  function testMergeUpdateExcept() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();

    db_merge('test_people')
      ->key(array('job' => 'Speaker'))
      ->insertFields(array('age' => 31))
      ->updateFields(array('name' => 'Tiffany'))
      ->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();
    $this->assertEqual($num_records_before, $num_records_after, 'Merge updated properly.');

    $person = db_query('SELECT * FROM {test_people} WHERE job = :job', array(':job' => 'Speaker'))->fetch();
    $this->assertEqual($person->name, 'Tiffany', 'Name set correctly.');
    $this->assertEqual($person->age, 30, 'Age skipped correctly.');
    $this->assertEqual($person->job, 'Speaker', 'Job set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
