# DatabaseTransactionTestCase::transactionOuterLayer()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3752–3779 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3752-L3779)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function transactionOuterLayer($suffix, $rollback = FALSE, $ddl_statement = FALSE)
```

## Documentation

```text
Helper method for transaction unit test.

This "outer layer" transaction starts and then encapsulates the
"inner layer" transaction. This nesting is used to evaluate whether the
database transaction API properly supports nesting. By "properly supports,"
we mean the outer transaction continues to exist regardless of what
functions are called and whether those functions start their own
transactions.

In contrast, a typical database would commit the outer transaction, start
a new transaction for the inner layer, commit the inner layer transaction,
and then be confused when the outer layer transaction tries to commit its
transaction (which was already committed when the inner transaction
started).

@param $suffix
  Suffix to add to field values to differentiate tests.
@param $rollback
  Whether or not to try rolling back the transaction when we're done.
@param $ddl_statement
  Whether to execute a DDL statement during the inner transaction.
```

## Code

```php
  protected function transactionOuterLayer($suffix, $rollback = FALSE, $ddl_statement = FALSE) {
    $connection = Database::getConnection();
    $depth = $connection->transactionDepth();
    $txn = db_transaction();

    // Insert a single row into the testing table.
    db_insert('test')
      ->fields(array(
        'name' => 'David' . $suffix,
        'age' => '24',
      ))
      ->execute();

    $this->assertTrue($connection->inTransaction(), 'In transaction before calling nested transaction.');

    // We're already in a transaction, but we call ->transactionInnerLayer
    // to nest another transaction inside the current one.
    $this->transactionInnerLayer($suffix, $rollback, $ddl_statement);

    $this->assertTrue($connection->inTransaction(), 'In transaction after calling nested transaction.');

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
