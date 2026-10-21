# DatabaseTasks_sqlite::validateDatabaseSettings()

- **Type:** Method
- **File:** [`includes/database/sqlite/install.inc`](../_file.md), lines 36–47 · [local source](../../../../../../source/includes/database/sqlite/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/install.inc#L36-L47)
- **Class:** [DatabaseTasks_sqlite](../DatabaseTasks_sqlite.md)

## Signature

```php
public function validateDatabaseSettings($database)
```

## Documentation

_No docblock in source._

## Code

```php
  public function validateDatabaseSettings($database) {
    // Perform standard validation.
    $errors = parent::validateDatabaseSettings($database);

    // Verify the database is writable.
    $db_directory = new SplFileInfo(dirname($database['database']));
    if (!$db_directory->isWritable()) {
      $errors[$database['driver'] . '][database'] = st('The directory you specified is not writable by the web server.');
    }

    return $errors;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
