# DatabaseStatementInterface

- **Type:** Interface
- **File:** [`includes/database/database.inc`](_file.md), lines 2068–2236 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2068-L2236)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
interface DatabaseStatementInterface extends Traversable
```

## Documentation

```text
Represents a prepared statement.

Some methods in that class are purposefully commented out. Due to a change in
how PHP defines PDOStatement, we can't define a signature for those methods
that will work the same way between versions older than 5.2.6 and later
versions.  See http://bugs.php.net/bug.php?id=42452 for more details.

Child implementations should either extend PDOStatement:
@code
class DatabaseStatement_oracle extends PDOStatement implements DatabaseStatementInterface {}
@endcode
or define their own class. If defining their own class, they will also have
to implement either the Iterator or IteratorAggregate interface before
DatabaseStatementInterface:
@code
class DatabaseStatement_oracle implements Iterator, DatabaseStatementInterface {}
@endcode
```

## Methods (derived index)

- [execute()](DatabaseStatementInterface/execute.md) — Executes a prepared statement
- [getQueryString()](DatabaseStatementInterface/getQueryString.md) — Gets the query string of this statement.
- [rowCount()](DatabaseStatementInterface/rowCount.md) — Returns the number of rows affected by the last SQL statement.
- [fetchField()](DatabaseStatementInterface/fetchField.md) — Returns a single field from the next record of a result set.
- [fetchAssoc()](DatabaseStatementInterface/fetchAssoc.md) — Fetches the next row and returns it as an associative array.
- [fetchCol()](DatabaseStatementInterface/fetchCol.md) — Returns an entire single column of a result set as an indexed array.
- [fetchAllKeyed()](DatabaseStatementInterface/fetchAllKeyed.md) — Returns the entire result set as a single associative array.
- [fetchAllAssoc()](DatabaseStatementInterface/fetchAllAssoc.md) — Returns the result set as an associative array keyed by the given field.

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
