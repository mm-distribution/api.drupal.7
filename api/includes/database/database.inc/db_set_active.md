# db_set_active()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2671–2673 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2671-L2673)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_set_active($key = 'default')
```

## Documentation

```text
Sets a new active database.

@param $key
  The key in the $databases array to set as the default database.

@return
  The key of the formerly active database.
```

## Code

```php
function db_set_active($key = 'default') {
  return Database::setActiveConnection($key);
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
