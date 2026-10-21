# DatabaseTransaction::rollback()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 2043–2046 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2043-L2046)
- **Class:** [DatabaseTransaction](../DatabaseTransaction.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function rollback()
```

## Documentation

```text
Rolls back the current transaction.

This is just a wrapper method to rollback whatever transaction stack we are
currently in, which is managed by the connection object itself. Note that
logging (preferable with watchdog_exception()) needs to happen after a
transaction has been rolled back or the log messages will be rolled back
too.

@see DatabaseConnection::rollback()
@see watchdog_exception()
```

## Code

```php
  public function rollback() {
    $this->rolledBack = TRUE;
    $this->connection->rollback($this->name);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
