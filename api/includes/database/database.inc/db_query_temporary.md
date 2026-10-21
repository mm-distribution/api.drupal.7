# db_query_temporary()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2524–2530 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2524-L2530)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_query_temporary($query, array $args = array(), array $options = array())
```

## Documentation

```text
Executes a SELECT query string and saves the result set to a temporary table.

The execution of the query string happens against the active database.

@param $query
  The prepared SELECT statement query to run. Although it will accept both
  named and unnamed placeholders, named placeholders are strongly preferred
  as they are more self-documenting.
@param $args
  An array of values to substitute into the query. If the query uses named
  placeholders, this is an associative array in any order. If the query uses
  unnamed placeholders (?), this is an indexed array and the order must match
  the order of placeholders in the query string.
@param $options
  An array of options to control how the query operates.

@return
  The name of the temporary table.

@see DatabaseConnection::defaultOptions()
```

## Code

```php
function db_query_temporary($query, array $args = array(), array $options = array()) {
  if (empty($options['target'])) {
    $options['target'] = 'default';
  }

  return Database::getConnection($options['target'])->queryTemporary($query, $args, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
