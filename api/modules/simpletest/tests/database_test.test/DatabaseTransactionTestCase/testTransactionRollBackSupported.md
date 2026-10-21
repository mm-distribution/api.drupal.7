# DatabaseTransactionTestCase::testTransactionRollBackSupported()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3844–3863 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3844-L3863)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTransactionRollBackSupported()
```

## Documentation

```text
Test transaction rollback on a database that supports transactions.

If the active connection does not support transactions, this test does nothing.
```

## Code

```php
  function testTransactionRollBackSupported() {
    // This test won't work right if transactions are not supported.
    if (!Database::getConnection()->supportsTransactions()) {
      return;
    }
    try {
      // Create two nested transactions. Roll back from the inner one.
      $this->transactionOuterLayer('B', TRUE);

      // Neither of the rows we inserted in the two transaction layers
      // should be present in the tables post-rollback.
      $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'DavidB'))->fetchField();
      $this->assertNotIdentical($saved_age, '24', 'Cannot retrieve DavidB row after commit.');
      $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'DanielB'))->fetchField();
      $this->assertNotIdentical($saved_age, '19', 'Cannot retrieve DanielB row after commit.');
    }
    catch (Exception $e) {
      $this->fail($e->getMessage());
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
