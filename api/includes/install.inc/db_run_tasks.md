# db_run_tasks()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 1331–1334 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L1331-L1334)

## Signature

```php
function db_run_tasks($driver)
```

## Documentation

```text
Ensures the environment for a Drupal database on a predefined connection.

This will run tasks that check that Drupal can perform all of the functions
on a database, that Drupal needs. Tasks include simple checks like CREATE
TABLE to database specific functions like stored procedures and client
encoding.
```

## Code

```php
function db_run_tasks($driver) {
  db_installer_object($driver)->runTasks();
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
