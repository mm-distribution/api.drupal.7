# db_installer_object()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1342–1346 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1342-L1346)

## Signature

```php
function db_installer_object($driver)
```

## Documentation

```text
Returns a database installer object.

@param $driver
  The name of the driver.
```

## Code

```php
function db_installer_object($driver) {
  Database::loadDriverFile($driver, array('install.inc'));
  $task_class = 'DatabaseTasks_' . $driver;
  return new $task_class();
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
