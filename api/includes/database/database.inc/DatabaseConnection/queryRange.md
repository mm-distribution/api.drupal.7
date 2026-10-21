# DatabaseConnection::queryRange()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1251–1251 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1251)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
abstract public function queryRange($query, $from, $count, array $args = array(), array $options = array());
```

## Documentation

```text
Runs a limited-range query on this database object.

Use this as a substitute for ->query() when a subset of the query is to be
returned. User-supplied arguments to the query should be passed in as
separate parameters so that they can be properly escaped to avoid SQL
injection attacks.

@param $query
  A string containing an SQL query.
@param $args
  An array of values to substitute into the query at placeholder markers.
@param $from
  The first result row to return.
@param $count
  The maximum number of result rows to return.
@param $options
  An array of options on the query.

@return DatabaseStatementInterface
  A database query result resource, or NULL if the query was not executed
  correctly.
```

## Code

```php
  abstract public function queryRange($query, $from, $count, array $args = array(), array $options = array());
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
