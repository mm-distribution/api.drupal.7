# DatabaseConnection::version()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1301–1303 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1301-L1303)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function version()
```

## Documentation

```text
Returns the version of the database server.
```

## Code

```php
  public function version() {
    return $this->connection->getAttribute(PDO::ATTR_SERVER_VERSION);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
