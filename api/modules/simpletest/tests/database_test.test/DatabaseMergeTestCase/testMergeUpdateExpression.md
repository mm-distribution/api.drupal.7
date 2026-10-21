# DatabaseMergeTestCase::testMergeUpdateExpression()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 1325–1349 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L1325-L1349)
- **Class:** [DatabaseMergeTestCase](../DatabaseMergeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMergeUpdateExpression()
```

## Documentation

```text
Confirm that we can merge-update a record successfully, with expressions.
```

## Code

```php
  function testMergeUpdateExpression() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();

    $age_before = db_query('SELECT age FROM {test_people} WHERE job = :job', array(':job' => 'Speaker'))->fetchField();

    // This is a very contrived example, as I have no idea why you'd want to
    // change age this way, but that's beside the point.
    // Note that we are also double-setting age here, once as a literal and
    // once as an expression. This test will only pass if the expression wins,
    // which is what is supposed to happen.
    db_merge('test_people')
      ->key(array('job' => 'Speaker'))
      ->fields(array('name' => 'Tiffany'))
      ->insertFields(array('age' => 31))
      ->expression('age', 'age + :age', array(':age' => 4))
      ->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test_people}')->fetchField();
    $this->assertEqual($num_records_before, $num_records_after, 'Merge updated properly.');

    $person = db_query('SELECT * FROM {test_people} WHERE job = :job', array(':job' => 'Speaker'))->fetch();
    $this->assertEqual($person->name, 'Tiffany', 'Name set correctly.');
    $this->assertEqual($person->age, $age_before + 4, 'Age updated correctly.');
    $this->assertEqual($person->job, 'Speaker', 'Job set correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
