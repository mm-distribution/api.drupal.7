# DatabaseConnection_sqlite::popTransaction()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 376–406 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L376-L406)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function popTransaction($name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function popTransaction($name) {
    if ($this->savepointSupport) {
      return parent::popTransaction($name);
    }
    if (!$this->supportsTransactions()) {
      return;
    }
    if (!$this->inTransaction()) {
      throw new DatabaseTransactionNoActiveException();
    }

    // Commit everything since SAVEPOINT $name.
    while($savepoint = array_pop($this->transactionLayers)) {
      if ($savepoint != $name) continue;

      // If there are no more layers left then we should commit or rollback.
      if (empty($this->transactionLayers)) {
        // If there was any rollback() we should roll back whole transaction.
        if ($this->willRollback) {
          $this->willRollback = FALSE;
          $this->connection->rollBack();
        }
        elseif (!$this->connection->commit()) {
          throw new DatabaseTransactionCommitFailedException();
        }
      }
      else {
        break;
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
