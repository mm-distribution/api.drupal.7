# DatabaseConnection::popTransaction()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1187–1202 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1187-L1202)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function popTransaction($name)
```

## Documentation

```text
Decreases the depth of transaction nesting.

If we pop off the last transaction layer, then we either commit or roll
back the transaction as necessary. If no transaction is active, we return
because the transaction may have manually been rolled back.

@param $name
  The name of the savepoint

@throws DatabaseTransactionNoActiveException
@throws DatabaseTransactionCommitFailedException

@see DatabaseTransaction
```

## Code

```php
  public function popTransaction($name) {
    if (!$this->supportsTransactions()) {
      return;
    }
    // The transaction has already been committed earlier. There is nothing we
    // need to do. If this transaction was part of an earlier out-of-order
    // rollback, an exception would already have been thrown by
    // Database::rollback().
    if (!isset($this->transactionLayers[$name])) {
      return;
    }

    // Mark this layer as committable.
    $this->transactionLayers[$name] = FALSE;
    $this->popCommittableTransactions();
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
