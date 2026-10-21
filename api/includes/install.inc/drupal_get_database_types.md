# drupal_get_database_types()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 253–283 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L253-L283)

## Signature

```php
function drupal_get_database_types()
```

## Documentation

```text
Returns all supported database installer objects that are compiled into PHP.

@return
 An array of database installer objects compiled into PHP.
```

## Code

```php
function drupal_get_database_types() {
  $databases = array();

  // We define a driver as a directory in /includes/database that in turn
  // contains a database.inc file. That allows us to drop in additional drivers
  // without modifying the installer.
  // Because we have no registry yet, we need to also include the install.inc
  // file for the driver explicitly.
  require_once DRUPAL_ROOT . '/includes/database/database.inc';
  foreach (file_scan_directory(DRUPAL_ROOT . '/includes/database', '/^[a-z]*$/i', array('recurse' => FALSE)) as $file) {
    if (file_exists($file->uri . '/database.inc') && file_exists($file->uri . '/install.inc')) {
      $drivers[$file->filename] = $file->uri;
    }
  }

  foreach ($drivers as $driver => $file) {
    $installer = db_installer_object($driver);
    if ($installer->installable()) {
      $databases[$driver] = $installer;
    }
  }

  // Usability: unconditionally put the MySQL driver on top.
  if (isset($databases['mysql'])) {
    $mysql_database = $databases['mysql'];
    unset($databases['mysql']);
    $databases = array('mysql' => $mysql_database) + $databases;
  }

  return $databases;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
