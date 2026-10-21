# DatabaseMergeTestCase::testMergeUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1253–1273 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1253-L1273)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeUpdate()
```

## Documentation

```text
Confirm that we can merge-update a record successfully.
```

## Code

```php
  function testMergeUpdate() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();

    $result = db_merge('test_people')
      ->key(array('job' => 'Speaker'))
      ->fields(array(
        'age' => 31,
        'name' => 'Tiffany',
      ))
      ->execute();

    $this->assertEqual($result, MergeQuery::STATUS_UPDATE, 'Update status returned.');

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();
    $this->assertEqual($num_records_before, $num_records_after, 'Merge updated properly.');

    $person = db_query('SELECT * FROM {test_people} WHERE job = :job', array(':job' => 'Speaker'))->fetch();
    $this->assertEqual($person->name, 'Tiffany', 'Name set correctly.');
    $this->assertEqual($person->age, 31, 'Age set correctly.');
    $this->assertEqual($person->job, 'Speaker', 'Job set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
