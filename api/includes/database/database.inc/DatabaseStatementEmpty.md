# DatabaseStatementEmpty

- **Type:** Class
- **File:** [`includes/database/database.inc`](_file.md), lines 2352–2427 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2352-L2427)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
class DatabaseStatementEmpty implements Iterator, DatabaseStatementInterface
```

## Documentation

```text
Empty implementation of a database statement.

This class satisfies the requirements of being a database statement/result
object, but does not actually contain data.  It is useful when developers
need to safely return an "empty" result set without connecting to an actual
database.  Calling code can then treat it the same as if it were an actual
result set that happens to contain no records.

@see SearchQuery
```

## Methods (derived index)

- [execute()](DatabaseStatementEmpty/execute.md)
- [getQueryString()](DatabaseStatementEmpty/getQueryString.md)
- [rowCount()](DatabaseStatementEmpty/rowCount.md)
- [setFetchMode()](DatabaseStatementEmpty/setFetchMode.md)
- [fetch()](DatabaseStatementEmpty/fetch.md)
- [fetchField()](DatabaseStatementEmpty/fetchField.md)
- [fetchObject()](DatabaseStatementEmpty/fetchObject.md)
- [fetchAssoc()](DatabaseStatementEmpty/fetchAssoc.md)
- [fetchAll()](DatabaseStatementEmpty/fetchAll.md)
- [fetchCol()](DatabaseStatementEmpty/fetchCol.md)
- [fetchAllKeyed()](DatabaseStatementEmpty/fetchAllKeyed.md)
- [fetchAllAssoc()](DatabaseStatementEmpty/fetchAllAssoc.md)
- [current()](DatabaseStatementEmpty/current.md)
- [key()](DatabaseStatementEmpty/key.md)
- [rewind()](DatabaseStatementEmpty/rewind.md)
- [next()](DatabaseStatementEmpty/next.md)
- [valid()](DatabaseStatementEmpty/valid.md)

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
