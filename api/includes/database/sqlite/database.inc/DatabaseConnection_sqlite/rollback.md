# DatabaseConnection_sqlite::rollback()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 326–358 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L326-L358)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function rollback($savepoint_name = 'drupal_transaction')
```

## Documentation

_No docblock in source._

## Code

```php
  public function rollback($savepoint_name = 'drupal_transaction') {
    if ($this->savepointSupport) {
      return parent::rollBack($savepoint_name);
    }

    if (!$this->inTransaction()) {
      throw new DatabaseTransactionNoActiveException();
    }
    // A previous rollback to an earlier savepoint may mean that the savepoint
    // in question has already been rolled back.
    if (!in_array($savepoint_name, $this->transactionLayers)) {
      return;
    }

    // We need to find the point we're rolling back to, all other savepoints
    // before are no longer needed.
    while ($savepoint = array_pop($this->transactionLayers)) {
      if ($savepoint == $savepoint_name) {
        // Mark whole stack of transactions as needed roll back.
        $this->willRollback = TRUE;
        // If it is the last the transaction in the stack, then it is not a
        // savepoint, it is the transaction itself so we will need to roll back
        // the transaction rather than a savepoint.
        if (empty($this->transactionLayers)) {
          break;
        }
        return;
      }
    }
    if ($this->supportsTransactions()) {
      $this->connection->rollBack();
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
