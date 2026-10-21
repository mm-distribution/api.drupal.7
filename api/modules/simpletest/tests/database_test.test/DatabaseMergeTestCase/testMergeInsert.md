# DatabaseMergeTestCase::testMergeInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1228–1248 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1228-L1248)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeInsert()
```

## Documentation

```text
Confirm that we can merge-insert a record successfully.
```

## Code

```php
  function testMergeInsert() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();

    $result = db_merge('test_people')
      ->key(array('job' => 'Presenter'))
      ->fields(array(
        'age' => 31,
        'name' => 'Tiffany',
      ))
      ->execute();

    $this->assertEqual($result, MergeQuery::STATUS_INSERT, 'Insert status returned.');

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();
    $this->assertEqual($num_records_before + 1, $num_records_after, 'Merge inserted properly.');

    $person = db_query('SELECT * FROM {test_people} WHERE job = :job', array(':job' => 'Presenter'))->fetch();
    $this->assertEqual($person->name, 'Tiffany', 'Name set correctly.');
    $this->assertEqual($person->age, 31, 'Age set correctly.');
    $this->assertEqual($person->job, 'Presenter', 'Job set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
