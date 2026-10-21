# DatabaseConnection::getLogger()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 614–616 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L614-L616)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function getLogger()
```

## Documentation

```text
Gets the current logging object for this connection.

@return DatabaseLog
  The current logging object for this connection. If there isn't one,
  NULL is returned.
```

## Code

```php
  public function getLogger() {
    return $this->logger;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
