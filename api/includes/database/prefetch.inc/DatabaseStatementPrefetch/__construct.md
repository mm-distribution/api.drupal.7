# DatabaseStatementPrefetch::__construct()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 128–132 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L128-L132)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function __construct(DatabaseConnection $connection, $query, array $driver_options = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct(DatabaseConnection $connection, $query, array $driver_options = array()) {
    $this->dbh = $connection;
    $this->queryString = $query;
    $this->driverOptions = $driver_options;
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
