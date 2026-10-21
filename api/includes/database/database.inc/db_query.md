# db_query()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2462–2468 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2462-L2468)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_query($query, array $args = array(), array $options = array())
```

## Documentation

```text
Executes an arbitrary query string against the active database.

Use this function for SELECT queries if it is just a simple query string.
If the caller or other modules need to change the query, use db_select()
instead.

Do not use this function for INSERT, UPDATE, or DELETE queries. Those should
be handled via db_insert(), db_update() and db_delete() respectively.

@param $query
  The prepared statement query to run. Although it will accept both named and
  unnamed placeholders, named placeholders are strongly preferred as they are
  more self-documenting.
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
function db_query($query, array $args = array(), array $options = array()) {
  if (empty($options['target'])) {
    $options['target'] = 'default';
  }

  return Database::getConnection($options['target'])->query($query, $args, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
