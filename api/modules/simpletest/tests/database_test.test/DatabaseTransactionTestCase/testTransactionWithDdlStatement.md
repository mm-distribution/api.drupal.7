# DatabaseTransactionTestCase::testTransactionWithDdlStatement()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3916–4006 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3916-L4006)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTransactionWithDdlStatement()
```

## Documentation

```text
Test the compatibility of transactions with DDL statements.
```

## Code

```php
  function testTransactionWithDdlStatement() {
    // First, test that a commit works normally, even with DDL statements.
    $transaction = db_transaction();
    $this->insertRow('row');
    $this->executeDDLStatement();
    unset($transaction);
    $this->assertRowPresent('row');

    // Even in different order.
    $this->cleanUp();
    $transaction = db_transaction();
    $this->executeDDLStatement();
    $this->insertRow('row');
    unset($transaction);
    $this->assertRowPresent('row');

    // Even with stacking.
    $this->cleanUp();
    $transaction = db_transaction();
    $transaction2 = db_transaction();
    $this->executeDDLStatement();
    unset($transaction2);
    $transaction3 = db_transaction();
    $this->insertRow('row');
    unset($transaction3);
    unset($transaction);
    $this->assertRowPresent('row');

    // A transaction after a DDL statement should still work the same.
    $this->cleanUp();
    $transaction = db_transaction();
    $transaction2 = db_transaction();
    $this->executeDDLStatement();
    unset($transaction2);
    $transaction3 = db_transaction();
    $this->insertRow('row');
    $transaction3->rollback();
    unset($transaction3);
    unset($transaction);
    $this->assertRowAbsent('row');

    // The behavior of a rollback depends on the type of database server.
    if (Database::getConnection()->supportsTransactionalDDL()) {
      // For database servers that support transactional DDL, a rollback
      // of a transaction including DDL statements should be possible.
      $this->cleanUp();
      $transaction = db_transaction();
      $this->insertRow('row');
      $this->executeDDLStatement();
      $transaction->rollback();
      unset($transaction);
      $this->assertRowAbsent('row');

      // Including with stacking.
      $this->cleanUp();
      $transaction = db_transaction();
      $transaction2 = db_transaction();
      $this->executeDDLStatement();
      unset($transaction2);
      $transaction3 = db_transaction();
      $this->insertRow('row');
      unset($transaction3);
      $transaction->rollback();
      unset($transaction);
      $this->assertRowAbsent('row');
    }
    else {
      // For database servers that do not support transactional DDL,
      // the DDL statement should commit the transaction stack.
      $this->cleanUp();
      $transaction = db_transaction();
      $this->insertRow('row');
      $this->executeDDLStatement();

      set_error_handler(array($this, 'rollBackWithoutTransactionErrorHandler'));
      try {
        // Rollback the outer transaction.
        $transaction->rollback();
        // @see \DatabaseConnection_mysql::rollback()
        if (PHP_VERSION_ID >= 80000) {
          $this->fail('Rolling back a transaction containing DDL should produce a warning.');
        }
      }
      catch (Exception $e) {
        $this->assertEqual('Rollback attempted when there is no active transaction.', $e->getMessage());
      }
      restore_error_handler();
      unset($transaction);
      $this->assertRowPresent('row');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
