# DatabaseConnection::pushTransaction()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1154–1170 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1154-L1170)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function pushTransaction($name)
```

## Documentation

```text
Increases the depth of transaction nesting.

If no transaction is already active, we begin a new transaction.

@throws DatabaseTransactionNameNonUniqueException

@see DatabaseTransaction
```

## Code

```php
  public function pushTransaction($name) {
    if (!$this->supportsTransactions()) {
      return;
    }
    if (isset($this->transactionLayers[$name])) {
      throw new DatabaseTransactionNameNonUniqueException($name . " is already in use.");
    }
    // If we're already in a transaction then we want to create a savepoint
    // rather than try to create another transaction.
    if ($this->inTransaction()) {
      $this->query('SAVEPOINT ' . $name);
    }
    else {
      $this->connection->beginTransaction();
    }
    $this->transactionLayers[$name] = $name;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
