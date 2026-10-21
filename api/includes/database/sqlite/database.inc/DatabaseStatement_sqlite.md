# DatabaseStatement_sqlite

- **Type:** Class
- **File:** [`includes/database/sqlite/database.inc`](_file.md), lines 426–550 · [local source](../../../../../source/includes/database/sqlite/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc#L426-L550)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
class DatabaseStatement_sqlite extends DatabaseStatementPrefetch implements Iterator, DatabaseStatementInterface
```

## Documentation

```text
Specific SQLite implementation of DatabaseConnection.

See DatabaseConnection_sqlite::PDOPrepare() for reasons why we must prefetch
the data instead of using PDOStatement.

@see DatabaseConnection_sqlite::PDOPrepare()
```

## Methods (derived index)

- [getStatement()](DatabaseStatement_sqlite/getStatement.md) — SQLite specific implementation of getStatement().
- [execute()](DatabaseStatement_sqlite/execute.md)

---
_Drupal 7.103 · [includes/database/sqlite/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
