# db_driver()

- **Type:** Function
- **File:** [`includes/database/database.inc`](_file.md), lines 2740–2742 · [local source](../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L2740-L2742)
- **Topics:** [database](../../../topics/database.md)

## Signature

```php
function db_driver()
```

## Documentation

```text
Retrieves the name of the currently active database driver.

@return
  The name of the currently active database driver.
```

## Code

```php
function db_driver() {
  return Database::getConnection()->driver();
}
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
