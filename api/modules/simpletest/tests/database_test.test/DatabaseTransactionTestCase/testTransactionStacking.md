# DatabaseTransactionTestCase::testTransactionStacking()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 4091–4199 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L4091-L4199)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTransactionStacking()
```

## Documentation

```text
Test transaction stacking and commit / rollback.
```

## Code

```php
  function testTransactionStacking() {
    // This test won't work right if transactions are not supported.
    if (!Database::getConnection()->supportsTransactions()) {
      return;
    }

    $database = Database::getConnection();

    // Standard case: pop the inner transaction before the outer transaction.
    $transaction = db_transaction();
    $this->insertRow('outer');
    $transaction2 = db_transaction();
    $this->insertRow('inner');
    // Pop the inner transaction.
    unset($transaction2);
    $this->assertTrue($database->inTransaction(), 'Still in a transaction after popping the inner transaction');
    // Pop the outer transaction.
    unset($transaction);
    $this->assertFalse($database->inTransaction(), 'Transaction closed after popping the outer transaction');
    $this->assertRowPresent('outer');
    $this->assertRowPresent('inner');

    // Pop the transaction in a different order they have been pushed.
    $this->cleanUp();
    $transaction = db_transaction();
    $this->insertRow('outer');
    $transaction2 = db_transaction();
    $this->insertRow('inner');
    // Pop the outer transaction, nothing should happen.
    unset($transaction);
    $this->insertRow('inner-after-outer-commit');
    $this->assertTrue($database->inTransaction(), 'Still in a transaction after popping the outer transaction');
    // Pop the inner transaction, the whole transaction should commit.
    unset($transaction2);
    $this->assertFalse($database->inTransaction(), 'Transaction closed after popping the inner transaction');
    $this->assertRowPresent('outer');
    $this->assertRowPresent('inner');
    $this->assertRowPresent('inner-after-outer-commit');

    // Rollback the inner transaction.
    $this->cleanUp();
    $transaction = db_transaction();
    $this->insertRow('outer');
    $transaction2 = db_transaction();
    $this->insertRow('inner');
    // Now rollback the inner transaction.
    $transaction2->rollback();
    unset($transaction2);
    $this->assertTrue($database->inTransaction(), 'Still in a transaction after popping the outer transaction');
    // Pop the outer transaction, it should commit.
    $this->insertRow('outer-after-inner-rollback');
    unset($transaction);
    $this->assertFalse($database->inTransaction(), 'Transaction closed after popping the inner transaction');
    $this->assertRowPresent('outer');
    $this->assertRowAbsent('inner');
    $this->assertRowPresent('outer-after-inner-rollback');

    // Rollback the inner transaction after committing the outer one.
    $this->cleanUp();
    $transaction = db_transaction();
    $this->insertRow('outer');
    $transaction2 = db_transaction();
    $this->insertRow('inner');
    // Pop the outer transaction, nothing should happen.
    unset($transaction);
    $this->assertTrue($database->inTransaction(), 'Still in a transaction after popping the outer transaction');
    // Now rollback the inner transaction, it should rollback.
    $transaction2->rollback();
    unset($transaction2);
    $this->assertFalse($database->inTransaction(), 'Transaction closed after popping the inner transaction');
    $this->assertRowPresent('outer');
    $this->assertRowAbsent('inner');

    // Rollback the outer transaction while the inner transaction is active.
    // In that case, an exception will be triggered because we cannot
    // ensure that the final result will have any meaning.
    $this->cleanUp();
    $transaction = db_transaction();
    $this->insertRow('outer');
    $transaction2 = db_transaction();
    $this->insertRow('inner');
    $transaction3 = db_transaction();
    $this->insertRow('inner2');
    // Rollback the outer transaction.
    try {
      $transaction->rollback();
      unset($transaction);
      $this->fail('Rolling back the outer transaction while the inner transaction is active resulted in an exception.');
    }
    catch (DatabaseTransactionOutOfOrderException $e) {
      $this->pass('Rolling back the outer transaction while the inner transaction is active resulted in an exception.');
    }
    $this->assertFalse($database->inTransaction(), 'No more in a transaction after rolling back the outer transaction');
    // Try to commit one inner transaction.
    unset($transaction3);
    $this->pass('Trying to commit an inner transaction resulted in an exception.');
    // Try to rollback one inner transaction.
    try {
      $transaction->rollback();
      unset($transaction2);
      $this->fail('Trying to commit an inner transaction resulted in an exception.');
    }
    catch (DatabaseTransactionNoActiveException $e) {
      $this->pass('Trying to commit an inner transaction resulted in an exception.');
    }
    $this->assertRowAbsent('outer');
    $this->assertRowAbsent('inner');
    $this->assertRowAbsent('inner2');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
