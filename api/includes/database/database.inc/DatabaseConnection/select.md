# DatabaseConnection::select()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 872–875 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L872-L875)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function select($table, $alias = NULL, array $options = array())
```

## Documentation

```text
Prepares and returns a SELECT query object.

@param $table
  The base table for this query, that is, the first table in the FROM
  clause. This table will also be used as the "base" table for query_alter
  hook implementations.
@param $alias
  The alias of the base table of this query.
@param $options
  An array of options on the query.

@return SelectQueryInterface
  An appropriate SelectQuery object for this database connection. Note that
  it may be a driver-specific subclass of SelectQuery, depending on the
  driver.

@see SelectQuery
```

## Code

```php
  public function select($table, $alias = NULL, array $options = array()) {
    $class = $this->getDriverClass('SelectQuery', array('query.inc', 'select.inc'));
    return new $class($table, $alias, $this, $options);
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
