# DatabaseConnection::driver()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1296–1296 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1296)
- **Class:** [DatabaseConnection](../DatabaseConnection.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
abstract public function driver();
```

## Documentation

```text
Returns the type of database driver.

This is not necessarily the same as the type of the database itself. For
instance, there could be two MySQL drivers, mysql and mysql_mock. This
function would return different values for each, but both would return
"mysql" for databaseType().
```

## Code

```php
  abstract public function driver();
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
