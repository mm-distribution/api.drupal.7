# TruncateQuery_sqlite

- **Type:** Class
- **File:** [`includes/database/sqlite/query.inc`](_file.md), lines 131–138 · [local source](../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L131-L138)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
class TruncateQuery_sqlite extends TruncateQuery
```

## Documentation

```text
SQLite specific implementation of TruncateQuery.

SQLite doesn't support TRUNCATE, but a DELETE query with no condition has
exactly the effect (it is implemented by DROPing the table).
```

## Methods (derived index)

- [__toString()](TruncateQuery_sqlite/__toString.md)

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
