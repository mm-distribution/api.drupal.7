# DatabaseMergeTestCase::testMergeInsertWithoutUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1354–1368 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1354-L1368)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeInsertWithoutUpdate()
```

## Documentation

```text
Test that we can merge-insert without any update fields.
```

## Code

```php
  function testMergeInsertWithoutUpdate() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();

    db_merge('test_people')
      ->key(array('job' => 'Presenter'))
      ->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();
    $this->assertEqual($num_records_before + 1, $num_records_after, 'Merge inserted properly.');

    $person = db_query('SELECT * FROM {test_people} WHERE job = :job', array(':job' => 'Presenter'))->fetch();
    $this->assertEqual($person->name, '', 'Name set correctly.');
    $this->assertEqual($person->age, 0, 'Age set correctly.');
    $this->assertEqual($person->job, 'Presenter', 'Job set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
