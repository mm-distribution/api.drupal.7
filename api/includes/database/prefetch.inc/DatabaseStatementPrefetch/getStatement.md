# DatabaseStatementPrefetch::getStatement()

- **Type:** Method
- **File:** [`includes/database/prefetch.inc`](../_file.md), lines 225–227 · [local source](../../../../../source/includes/database/prefetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc#L225-L227)
- **Class:** [DatabaseStatementPrefetch](../DatabaseStatementPrefetch.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
protected function getStatement($query, &$args = array())
```

## Documentation

```text
Grab a PDOStatement object from a given query and its arguments.

Some drivers (including SQLite) will need to perform some preparation
themselves to get the statement right.

@param $query
  The query.
@param array $args
  An array of arguments.
@return PDOStatement
  A PDOStatement object.
```

## Code

```php
  protected function getStatement($query, &$args = array()) {
    return $this->dbh->prepare($query);
  }
```

---
_Drupal 7.103 · [includes/database/prefetch.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/prefetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
