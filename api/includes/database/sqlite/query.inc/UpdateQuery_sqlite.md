# UpdateQuery_sqlite

- **Type:** Class
- **File:** [`includes/database/sqlite/query.inc`](_file.md), lines 68–101 · [local source](../../../../../source/includes/database/sqlite/query.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc#L68-L101)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
class UpdateQuery_sqlite extends UpdateQuery
```

## Documentation

```text
SQLite specific implementation of UpdateQuery.

SQLite counts all the rows that match the conditions as modified, even if they
will not be affected by the query. We workaround this by ensuring that
we don't select those rows.

A query like this one:
  UPDATE test SET col1 = 'newcol1', col2 = 'newcol2' WHERE tid = 1
will become:
  UPDATE test SET col1 = 'newcol1', col2 = 'newcol2' WHERE tid = 1 AND (col1 <> 'newcol1' OR col2 <> 'newcol2')
```

## Methods (derived index)

- [execute()](UpdateQuery_sqlite/execute.md)

---
_Drupal 7.103 · [includes/database/sqlite/query.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/query.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
