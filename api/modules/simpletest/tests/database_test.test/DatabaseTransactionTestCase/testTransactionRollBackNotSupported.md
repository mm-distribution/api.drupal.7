# DatabaseTransactionTestCase::testTransactionRollBackNotSupported()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3870–3889 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3870-L3889)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTransactionRollBackNotSupported()
```

## Documentation

```text
Test transaction rollback on a database that does not support transactions.

If the active driver supports transactions, this test does nothing.
```

## Code

```php
  function testTransactionRollBackNotSupported() {
    // This test won't work right if transactions are supported.
    if (Database::getConnection()->supportsTransactions()) {
      return;
    }
    try {
      // Create two nested transactions. Attempt to roll back from the inner one.
      $this->transactionOuterLayer('B', TRUE);

      // Because our current database claims to not support transactions,
      // the inserted rows should be present despite the attempt to roll back.
      $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'DavidB'))->fetchField();
      $this->assertIdentical($saved_age, '24', 'DavidB not rolled back, since transactions are not supported.');
      $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'DanielB'))->fetchField();
      $this->assertIdentical($saved_age, '19', 'DanielB not rolled back, since transactions are not supported.');
    }
    catch (Exception $e) {
      $this->fail($e->getMessage());
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
