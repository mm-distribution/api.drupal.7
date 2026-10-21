# db_transaction()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2655–2660 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2655-L2660)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_transaction($name = NULL, array $options = array())
```

## Documentation

```text
Returns a new transaction object for the active database.

@param string $name
  Optional name of the transaction.
@param array $options
  An array of options to control how the transaction operates:
  - target: The database target name.

@return DatabaseTransaction
  A new DatabaseTransaction object for this connection.
```

## Code

```php
function db_transaction($name = NULL, array $options = array()) {
  if (empty($options['target'])) {
    $options['target'] = 'default';
  }
  return Database::getConnection($options['target'])->startTransaction($name);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
