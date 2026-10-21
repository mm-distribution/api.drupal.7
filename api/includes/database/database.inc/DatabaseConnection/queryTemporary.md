# DatabaseConnection::queryTemporary()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1286–1286 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1286)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
abstract function queryTemporary($query, array $args = array(), array $options = array());
```

## Documentation

```text
Runs a SELECT query and stores its results in a temporary table.

Use this as a substitute for ->query() when the results need to stored
in a temporary table. Temporary tables exist for the duration of the page
request. User-supplied arguments to the query should be passed in as
separate parameters so that they can be properly escaped to avoid SQL
injection attacks.

Note that if you need to know how many results were returned, you should do
a SELECT COUNT(*) on the temporary table afterwards.

@param $query
  A string containing a normal SELECT SQL query.
@param $args
  An array of values to substitute into the query at placeholder markers.
@param $options
  An associative array of options to control how the query is run. See
  the documentation for DatabaseConnection::defaultOptions() for details.

@return
  The name of the temporary table.
```

## Code

```php
  abstract function queryTemporary($query, array $args = array(), array $options = array());
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
