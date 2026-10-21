# Database::parseConnectionInfo()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1622–1665 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1622-L1665)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
final public static function parseConnectionInfo()
```

## Documentation

```text
Process the configuration file for database information.
```

## Code

```php
  final public static function parseConnectionInfo() {
    global $databases;

    $database_info = is_array($databases) ? $databases : array();
    foreach ($database_info as $index => $info) {
      foreach ($database_info[$index] as $target => $value) {
        // If there is no "driver" property, then we assume it's an array of
        // possible connections for this target. Pick one at random. That allows
        //  us to have, for example, multiple slave servers.
        if (empty($value['driver'])) {
          $database_info[$index][$target] = $database_info[$index][$target][mt_rand(0, count($database_info[$index][$target]) - 1)];
        }

        // Parse the prefix information.
        if (!isset($database_info[$index][$target]['prefix'])) {
          // Default to an empty prefix.
          $database_info[$index][$target]['prefix'] = array(
            'default' => '',
          );
        }
        elseif (!is_array($database_info[$index][$target]['prefix'])) {
          // Transform the flat form into an array form.
          $database_info[$index][$target]['prefix'] = array(
            'default' => $database_info[$index][$target]['prefix'],
          );
        }
      }
    }

    if (!is_array(self::$databaseInfo)) {
      self::$databaseInfo = $database_info;
    }

    // Merge the new $database_info into the existing.
    // array_merge_recursive() cannot be used, as it would make multiple
    // database, user, and password keys in the same database array.
    else {
      foreach ($database_info as $database_key => $database_values) {
        foreach ($database_values as $target => $target_values) {
          self::$databaseInfo[$database_key][$target] = $target_values;
        }
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
