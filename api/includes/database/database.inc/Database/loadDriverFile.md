# Database::loadDriverFile()

- **Type:** Method
- **File:** [`includes/database/database.inc`](../_file.md), lines 1869–1888 · [local source](../../../../../source/includes/database/database.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc#L1869-L1888)
- **Class:** [Database](../Database.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public static function loadDriverFile($driver, array $files = array())
```

## Documentation

```text
Load a file for the database that might hold a class.

@param $driver
  The name of the driver.
@param array $files
  The name of the files the driver specific class can be.
```

## Code

```php
  public static function loadDriverFile($driver, array $files = array()) {
    static $base_path;

    if (empty($base_path)) {
      $base_path = dirname(realpath(__FILE__));
    }

    $driver_base_path = "$base_path/$driver";
    foreach ($files as $file) {
      // Load the base file first so that classes extending base classes will
      // have the base class loaded.
      foreach (array("$base_path/$file", "$driver_base_path/$file") as $filename) {
        // The OS caches file_exists() and PHP caches require_once(), so
        // we'll let both of those take care of performance here.
        if (file_exists($filename)) {
          require_once $filename;
        }
      }
    }
  }
```

---
_Drupal 7.103 · [includes/database/database.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/database.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
