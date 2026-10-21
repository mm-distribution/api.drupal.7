# DatabaseConnection_sqlite::databaseType()

- **Type:** Method
- **File:** [`includes/database/sqlite/database.inc`](../_file.md), lines 288–290 · [local source](../../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L288-L290)
- **Class:** [DatabaseConnection_sqlite](../DatabaseConnection_sqlite.md)
- **Topics:** [database](../../../../../topics/database.md)

## Signature

```php
public function databaseType()
```

## Documentation

_No docblock in source._

## Code

```php
  public function databaseType() {
    return 'sqlite';
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
