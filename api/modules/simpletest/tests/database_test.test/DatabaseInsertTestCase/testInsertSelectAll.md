# DatabaseInsertTestCase::testInsertSelectAll()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 705–721 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L705-L721)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInsertSelectAll()
```

## Documentation

```text
Tests that the INSERT INTO ... SELECT * ... syntax works.
```

## Code

```php
  function testInsertSelectAll() {
    $query = db_select('test_people', 'tp')
      ->fields('tp')
      ->condition('tp.name', 'Meredith');

    // The resulting query should be equivalent to:
    // INSERT INTO test_people_copy
    // SELECT *
    // FROM test_people tp
    // WHERE tp.name = 'Meredith'
    db_insert('test_people_copy')
      ->from($query)
      ->execute();

    $saved_age = db_query('SELECT age FROM {test_people_copy} WHERE name = :name', array(':name' => 'Meredith'))->fetchField();
    $this->assertIdentical($saved_age, '30', 'Can retrieve after inserting.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
