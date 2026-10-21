# DatabaseInsertTestCase::testMultiInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 577–605 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L577-L605)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMultiInsert()
```

## Documentation

```text
Test that we can insert multiple records in one query object.
```

## Code

```php
  function testMultiInsert() {
    $num_records_before = (int) db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    $query = db_insert('test');
    $query->fields(array(
      'name' => 'Larry',
      'age' => '30',
    ));

    // We should be able to specify values in any order if named.
    $query->values(array(
      'age' => '31',
      'name' => 'Curly',
    ));

    // We should be able to say "use the field order".
    // This is not the recommended mechanism for most cases, but it should work.
    $query->values(array('Moe', '32'));
    $query->execute();

    $num_records_after = (int) db_query('SELECT COUNT(*) FROM {test}')->fetchField();
    $this->assertIdentical($num_records_before + 3, $num_records_after, 'Record inserts correctly.');
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
