# DatabaseInsertTestCase::testRepeatedInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 610–640 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L610-L640)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRepeatedInsert()
```

## Documentation

```text
Test that an insert object can be reused with new data after it executes.
```

## Code

```php
  function testRepeatedInsert() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    $query = db_insert('test');

    $query->fields(array(
      'name' => 'Larry',
      'age' => '30',
    ));
    $query->execute();  // This should run the insert, but leave the fields intact.

    // We should be able to specify values in any order if named.
    $query->values(array(
      'age' => '31',
      'name' => 'Curly',
    ));
    $query->execute();

    // We should be able to say "use the field order".
    $query->values(array('Moe', '32'));
    $query->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test}')->fetchField();
    $this->assertIdentical((int) $num_records_before + 3, (int) $num_records_after, 'Record inserts correctly.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Larry'))->fetchField();
    $this->assertIdentical($saved_age, '30', 'Can retrieve after inserting.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Curly'))->fetchField();
    $this->assertIdentical($saved_age, '31', 'Can retrieve after inserting.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Moe'))->fetchField();
    $this->assertIdentical($saved_age, '32', 'Can retrieve after inserting.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
