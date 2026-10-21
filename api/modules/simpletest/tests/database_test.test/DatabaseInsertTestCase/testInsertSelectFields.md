# DatabaseInsertTestCase::testInsertSelectFields()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 679–700 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L679-L700)
- **Class:** [DatabaseInsertTestCase](../DatabaseInsertTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testInsertSelectFields()
```

## Documentation

```text
Test that the INSERT INTO ... SELECT (fields) ... syntax works.
```

## Code

```php
  function testInsertSelectFields() {
    $query = db_select('test_people', 'tp');
    // The query builder will always append expressions after fields.
    // Add the expression first to test that the insert fields are correctly
    // re-ordered.
    $query->addExpression('tp.age', 'age');
    $query
      ->fields('tp', array('name','job'))
      ->condition('tp.name', 'Meredith');

    // The resulting query should be equivalent to:
    // INSERT INTO test (age, name, job)
    // SELECT tp.age AS age, tp.name AS name, tp.job AS job
    // FROM test_people tp
    // WHERE tp.name = 'Meredith'
    db_insert('test')
      ->from($query)
      ->execute();

    $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'Meredith'))->fetchField();
    $this->assertIdentical($saved_age, '30', 'Can retrieve after inserting.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
