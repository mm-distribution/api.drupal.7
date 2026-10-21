# DatabaseMergeTestCase::testMergeUpdateExplicit()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1299–1320 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1299-L1320)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeUpdateExplicit()
```

## Documentation

```text
Confirm that we can merge-update a record successfully, with alternate replacement.
```

## Code

```php
  function testMergeUpdateExplicit() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();

    db_merge('test_people')
      ->key(array('job' => 'Speaker'))
      ->insertFields(array(
        'age' => 31,
        'name' => 'Tiffany',
      ))
      ->updateFields(array(
        'name' => 'Joe',
      ))
      ->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();
    $this->assertEqual($num_records_before, $num_records_after, 'Merge updated properly.');

    $person = db_query('SELECT * FROM {test_people} WHERE job = :job', array(':job' => 'Speaker'))->fetch();
    $this->assertEqual($person->name, 'Joe', 'Name set correctly.');
    $this->assertEqual($person->age, 30, 'Age skipped correctly.');
    $this->assertEqual($person->job, 'Speaker', 'Job set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
