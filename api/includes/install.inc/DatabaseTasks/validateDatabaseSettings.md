# DatabaseTasks::validateDatabaseSettings()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 560–574 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L560-L574)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
public function validateDatabaseSettings($database)
```

## Documentation

```text
Validates driver specific configuration settings.

Checks to ensure correct basic database settings and that a proper
connection to the database can be established.

@param $database
  An array of driver specific configuration options.

@return
  An array of driver configuration errors, keyed by form element name.
```

## Code

```php
  public function validateDatabaseSettings($database) {
    $errors = array();

    // Verify the table prefix.
    if (!empty($database['prefix']) && is_string($database['prefix']) && !preg_match('/^[A-Za-z0-9_.]+$/', $database['prefix'])) {
      $errors[$database['driver'] . '][advanced_options][db_prefix'] = st('The database table prefix you have entered, %prefix, is invalid. The table prefix can only contain alphanumeric characters, periods, or underscores.', array('%prefix' => $database['prefix']));
    }

    // Verify the database port.
    if (!empty($database['port']) && !is_numeric($database['port'])) {
      $errors[$database['driver'] . '][advanced_options][port'] =  st('Database port must be a number.');
    }

    return $errors;
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
