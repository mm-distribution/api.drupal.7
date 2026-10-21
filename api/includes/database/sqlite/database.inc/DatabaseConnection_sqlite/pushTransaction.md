# DatabaseConnection_sqlite::pushTransaction()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 360–374 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L360-L374)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function pushTransaction($name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function pushTransaction($name) {
    if ($this->savepointSupport) {
      return parent::pushTransaction($name);
    }
    if (!$this->supportsTransactions()) {
      return;
    }
    if (isset($this->transactionLayers[$name])) {
      throw new DatabaseTransactionNameNonUniqueException($name . " is already in use.");
    }
    if (!$this->inTransaction()) {
      $this->connection->beginTransaction();
    }
    $this->transactionLayers[$name] = $name;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
