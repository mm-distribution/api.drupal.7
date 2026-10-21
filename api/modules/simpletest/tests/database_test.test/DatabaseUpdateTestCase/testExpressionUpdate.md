# DatabaseUpdateTestCase::testExpressionUpdate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 927–958 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L927-L958)
- **Class:** [DatabaseUpdateTestCase](../DatabaseUpdateTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testExpressionUpdate()
```

## Documentation

```text
Test updating with expressions.
```

## Code

```php
  function testExpressionUpdate() {
    // Set age = 1 for a single row for this test to work.
    db_update('test')
      ->condition('id', 1)
      ->fields(array('age' => 1))
      ->execute();

    // Ensure that expressions are handled properly. This should set every
    // record's age to a square of itself. The number of affected rows returned
    // by db_update() will vary across different database engines and versions:
    // - MySQL / InnoDB: changed rows only
    // - MySQL / MyISAM: changed rows only
    // - PostgreSQL: all rows matched by the query
    // - SQLite: changed rows only (see workaround in UpdateQuery_sqlite)
    // All database engines will change only three of the four records in the
    // table since 1*1 = 1. However, the pgsql driver will return the number of
    // rows matched rather than the number changed.
    // @see https://www.drupal.org/project/drupal/issues/805858
    // @see https://www.drupal.org/project/drupal/issues/3264471
    $connection = Database::getConnection()->getConnectionOptions();
    $expected_rows = 3;
    if ($connection['driver'] === 'pgsql') {
      $expected_rows ++;
    }
    $num_rows = db_update('test')
      ->expression('age', 'age * age')
      ->execute();
    $this->assertIdentical($num_rows, $expected_rows, 'Number of affected rows are returned.');

    $saved_name = db_query('SELECT name FROM {test} WHERE age = :age', array(':age' => pow(26, 2)))->fetchField();
    $this->assertIdentical('Paul', $saved_name, 'Successfully updated values using an algebraic expression.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
