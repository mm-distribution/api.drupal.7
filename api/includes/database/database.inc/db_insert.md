# db_insert()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2543–2548 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2543-L2548)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_insert($table, array $options = array())
```

## Documentation

```text
Returns a new InsertQuery object for the active database.

@param $table
  The table into which to insert.
@param $options
  An array of options to control how the query operates.

@return InsertQuery
  A new InsertQuery object for this connection.
```

## Code

```php
function db_insert($table, array $options = array()) {
  if (empty($options['target']) || $options['target'] == 'slave') {
    $options['target'] = 'default';
  }
  return Database::getConnection($options['target'])->insert($table, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
