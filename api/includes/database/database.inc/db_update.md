# db_update()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2579–2584 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2579-L2584)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_update($table, array $options = array())
```

## Documentation

```text
Returns a new UpdateQuery object for the active database.

@param $table
  The table to update.
@param $options
  An array of options to control how the query operates.

@return UpdateQuery
  A new UpdateQuery object for this connection.
```

## Code

```php
function db_update($table, array $options = array()) {
  if (empty($options['target']) || $options['target'] == 'slave') {
    $options['target'] = 'default';
  }
  return Database::getConnection($options['target'])->update($table, $options);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
