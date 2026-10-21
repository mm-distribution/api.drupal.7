# install_database_errors()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 972–1004 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L972-L1004)

## Signature

```php
function install_database_errors($database, $settings_file)
```

## Documentation

```text
Checks a database connection and returns any errors.
```

## Code

```php
function install_database_errors($database, $settings_file) {
  global $databases;
  $errors = array();

  // Check database type.
  $database_types = drupal_get_database_types();
  $driver = $database['driver'];
  if (!isset($database_types[$driver])) {
    $errors['driver'] = st("In your %settings_file file you have configured @drupal to use a %driver server, however your PHP installation currently does not support this database type.", array('%settings_file' => $settings_file, '@drupal' => drupal_install_profile_distribution_name(), '%driver' => $driver));
  }
  else {
    // Run driver specific validation
    $errors += $database_types[$driver]->validateDatabaseSettings($database);

    // Run tasks associated with the database type. Any errors are caught in the
    // calling function.
    $databases['default']['default'] = $database;
    // Just changing the global doesn't get the new information processed.
    // We tell tell the Database class to re-parse $databases.
    Database::parseConnectionInfo();

    try {
      db_run_tasks($driver);
    }
    catch (DatabaseTaskException $e) {
      // These are generic errors, so we do not have any specific key of the
      // database connection array to attach them to; therefore, we just put
      // them in the error array with standard numeric keys.
      $errors[$driver . '][0'] = $e->getMessage();
    }
  }
  return $errors;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
