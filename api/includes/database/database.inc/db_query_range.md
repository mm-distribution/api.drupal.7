# db_query_range()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2494–2500 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2494-L2500)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_query_range($query, $from, $count, array $args = array(), array $options = array())
```

## Documentation

```text
Executes a query against the active database, restricted to a range.

@param $query
  The prepared statement query to run. Although it will accept both named and
  unnamed placeholders, named placeholders are strongly preferred as they are
  more self-documenting.
@param $from
  The first record from the result set to return.
@param $count
  The number of records to return from the result set.
@param $args
  An array of values to substitute into the query. If the query uses named
  placeholders, this is an associative array in any order. If the query uses
  unnamed placeholders (?), this is an indexed array and the order must match
  the order of placeholders in the query string.
@param $options
  An array of options to control how the query operates.

@return DatabaseStatementInterface
  A prepared statement object, already executed.

@see DatabaseConnection::defaultOptions()
```

## Code

```php
function db_query_range($query, $from, $count, array $args = array(), array $options = array()) {
  if (empty($options['target'])) {
    $options['target'] = 'default';
  }

  return Database::getConnection($options['target'])->queryRange($query, $from, $count, $args, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
