# db_select()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2636–2641 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2636-L2641)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_select($table, $alias = NULL, array $options = array())
```

## Documentation

```text
Returns a new SelectQuery object for the active database.

@param $table
  The base table for this query. May be a string or another SelectQuery
  object. If a query object is passed, it will be used as a subselect.
@param $alias
  The alias for the base table of this query.
@param $options
  An array of options to control how the query operates.

@return SelectQuery
  A new SelectQuery object for this connection.
```

## Code

```php
function db_select($table, $alias = NULL, array $options = array()) {
  if (empty($options['target'])) {
    $options['target'] = 'default';
  }
  return Database::getConnection($options['target'])->select($table, $alias, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
