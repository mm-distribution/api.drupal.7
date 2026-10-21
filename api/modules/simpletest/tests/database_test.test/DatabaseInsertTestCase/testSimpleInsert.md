# DatabaseInsertTestCase::testSimpleInsert()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 558–572 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L558-L572)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSimpleInsert()
```

## Documentation

```text
Test the very basic insert functionality.
```

## Code

```php
  function testSimpleInsert() {
    $num_records_before = db_query('SELECT COUNT(*) FROM {test}')->fetchField();

    $query = db_insert('test');
    $query->fields(array(
      'name' => 'Yoko',
      'age' => '29',
    ));
    $query->execute();

    $num_records_after = db_query('SELECT COUNT(*) FROM {test}')->fetchField();
    $this->assertIdentical($num_records_before + 1, (int) $num_records_after, 'Record inserts correctly.');
    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Yoko'))->fetchField();
    $this->assertIdentical($saved_age, '29', 'Can retrieve after inserting.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
