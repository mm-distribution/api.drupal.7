# InsertQuery_sqlite

- **Type:** Class
- **File:** [`includes/database/sqlite/query.inc`](_file.md), lines 20–54 · [local source](../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L20-L54)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
class InsertQuery_sqlite extends InsertQuery
```

## Documentation

```text
SQLite specific implementation of InsertQuery.

We ignore all the default fields and use the clever SQLite syntax:
  INSERT INTO table DEFAULT VALUES
for degenerated "default only" queries.
```

## Methods (derived index)

- [execute()](InsertQuery_sqlite/execute.md)
- [__toString()](InsertQuery_sqlite/__toString.md)

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
