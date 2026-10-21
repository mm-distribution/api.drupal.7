# drupal_get_installed_schema_version()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 146–167 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L146-L167)

## Signature

```php
function drupal_get_installed_schema_version($module, $reset = FALSE, $array = FALSE)
```

## Documentation

```text
Returns the currently installed schema version for a module.

@param $module
  A module name.
@param $reset
  Set to TRUE after modifying the system table.
@param $array
  Set to TRUE if you want to get information about all modules in the
  system.
@return
  The currently installed schema version, or SCHEMA_UNINSTALLED if the
  module is not installed.
```

## Code

```php
function drupal_get_installed_schema_version($module, $reset = FALSE, $array = FALSE) {
  static $versions = array();

  if ($reset) {
    $versions = array();
  }

  if (!$versions) {
    $versions = array();
    $result = db_query("SELECT name, schema_version FROM {system} WHERE type = :type", array(':type' => 'module'));
    foreach ($result as $row) {
      $versions[$row->name] = $row->schema_version;
    }
  }

  if ($array) {
    return $versions;
  }
  else {
    return isset($versions[$module]) ? $versions[$module] : SCHEMA_UNINSTALLED;
  }
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
