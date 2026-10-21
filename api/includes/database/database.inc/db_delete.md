# db_delete()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2597–2602 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2597-L2602)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_delete($table, array $options = array())
```

## Documentation

```text
Returns a new DeleteQuery object for the active database.

@param $table
  The table from which to delete.
@param $options
  An array of options to control how the query operates.

@return DeleteQuery
  A new DeleteQuery object for this connection.
```

## Code

```php
function db_delete($table, array $options = array()) {
  if (empty($options['target']) || $options['target'] == 'slave') {
    $options['target'] = 'default';
  }
  return Database::getConnection($options['target'])->delete($table, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
