# DatabaseTransactionTestCase::testCommittedTransaction()

- **Type:** Method
- **File:** [`modules/simpletest/tests/database_test.test`](../_file.md), lines 3897–3911 · [local source](../../../../../../source/modules/simpletest/tests/database_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test#L3897-L3911)
- **Class:** [DatabaseTransactionTestCase](../DatabaseTransactionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCommittedTransaction()
```

## Documentation

```text
Test committed transaction.

The behavior of this test should be identical for connections that support
transactions and those that do not.
```

## Code

```php
  function testCommittedTransaction() {
    try {
      // Create two nested transactions. The changes should be committed.
      $this->transactionOuterLayer('A');

      // Because we committed, both of the inserted rows should be present.
      $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'DavidA'))->fetchField();
      $this->assertIdentical($saved_age, '24', 'Can retrieve DavidA row after commit.');
      $saved_age = db_query('SELECT age FROM {test} WHERE name = :name', array(':name' => 'DanielA'))->fetchField();
      $this->assertIdentical($saved_age, '19', 'Can retrieve DanielA row after commit.');
    }
    catch (Exception $e) {
      $this->fail($e->getMessage());
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
