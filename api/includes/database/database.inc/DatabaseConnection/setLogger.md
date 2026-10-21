# DatabaseConnection::setLogger()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 603–605 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L603-L605)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function setLogger(DatabaseLog $logger)
```

## Documentation

```text
Associates a logging object with this connection.

@param $logger
  The logging object we want to use.
```

## Code

```php
  public function setLogger(DatabaseLog $logger) {
    $this->logger = $logger;
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
