# DatabaseTransactionTestCase::transactionInnerLayer()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3792–3837 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3792-L3837)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function transactionInnerLayer($suffix, $rollback = FALSE, $ddl_statement = FALSE)
```

## Documentation

```text
Helper method for transaction unit tests. This "inner layer" transaction
is either used alone or nested inside of the "outer layer" transaction.

@param $suffix
  Suffix to add to field values to differentiate tests.
@param $rollback
  Whether or not to try rolling back the transaction when we're done.
@param $ddl_statement
  Whether to execute a DDL statement during the transaction.
```

## Code

```php
  protected function transactionInnerLayer($suffix, $rollback = FALSE, $ddl_statement = FALSE) {
    $connection = Database::getConnection();

    $depth = $connection->transactionDepth();
    // Start a transaction. If we're being called from ->transactionOuterLayer,
    // then we're already in a transaction. Normally, that would make starting
    // a transaction here dangerous, but the database API handles this problem
    // for us by tracking the nesting and avoiding the danger.
    $txn = db_transaction();

    $depth2 = $connection->transactionDepth();
    $this->assertTrue($depth < $depth2, 'Transaction depth is has increased with new transaction.');

    // Insert a single row into the testing table.
    db_insert('test')
      ->fields(array(
        'name' => 'Daniel' . $suffix,
        'age' => '19',
      ))
      ->execute();

    $this->assertTrue($connection->inTransaction(), 'In transaction inside nested transaction.');

    if ($ddl_statement) {
      $table = array(
        'fields' => array(
          'id' => array(
            'type' => 'serial',
            'unsigned' => TRUE,
            'not null' => TRUE,
          ),
        ),
        'primary key' => array('id'),
      );
      db_create_table('database_test_1', $table);

      $this->assertTrue($connection->inTransaction(), 'In transaction inside nested transaction.');
    }

    if ($rollback) {
      // Roll back the transaction, if requested.
      // This rollback should propagate to the last savepoint.
      $txn->rollback();
      $this->assertTrue(($connection->transactionDepth() == $depth), 'Transaction has rolled back to the last savepoint after calling rollback().');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
