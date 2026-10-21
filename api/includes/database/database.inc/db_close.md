# db_close()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2751–2756 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2751-L2756)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_close(array $options = array())
```

## Documentation

```text
Closes the active database connection.

@param $options
  An array of options to control which connection is closed. Only the target
  key has any meaning in this case.
```

## Code

```php
function db_close(array $options = array()) {
  if (empty($options['target'])) {
    $options['target'] = NULL;
  }
  Database::closeConnection($options['target']);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
