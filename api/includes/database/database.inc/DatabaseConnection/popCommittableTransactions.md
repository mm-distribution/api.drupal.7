# DatabaseConnection::popCommittableTransactions()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1207–1226 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1207-L1226)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function popCommittableTransactions()
```

## Documentation

```text
Internal function: commit all the transaction layers that can commit.
```

## Code

```php
  protected function popCommittableTransactions() {
    // Commit all the committable layers.
    foreach (array_reverse($this->transactionLayers) as $name => $active) {
      // Stop once we found an active transaction.
      if ($active) {
        break;
      }

      // If there are no more layers left then we should commit.
      unset($this->transactionLayers[$name]);
      if (empty($this->transactionLayers)) {
        if (!$this->connection->commit()) {
          throw new DatabaseTransactionCommitFailedException();
        }
      }
      else {
        $this->query('RELEASE SAVEPOINT ' . $name);
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
