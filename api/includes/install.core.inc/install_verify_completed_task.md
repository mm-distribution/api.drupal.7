# install_verify_completed_task()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 828–844 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L828-L844)

## Signature

```php
function install_verify_completed_task()
```

## Documentation

```text
Verifies and returns the last installation task that was completed.

@return
  The last completed task, if there is one. An exception is thrown if Drupal
  is already installed.
```

## Code

```php
function install_verify_completed_task() {
  try {
    if ($result = db_query("SELECT value FROM {variable} WHERE name = :name", array('name' => 'install_task'))) {
      $task = unserialize($result->fetchField());
    }
  }
  // Do not trigger an error if the database query fails, since the database
  // might not be set up yet.
  catch (Exception $e) {
  }
  if (isset($task)) {
    if ($task == 'done') {
      throw new Exception(install_already_done_error());
    }
    return $task;
  }
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
