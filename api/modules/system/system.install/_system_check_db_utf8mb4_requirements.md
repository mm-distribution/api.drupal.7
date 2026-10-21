# _system_check_db_utf8mb4_requirements()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 603–661 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L603-L661)
- **Module/theme:** system

## Signature

```php
function _system_check_db_utf8mb4_requirements($phase)
```

## Documentation

```text
Checks whether the requirements for multi-byte UTF-8 support are met.

@param string $phase
  The hook_requirements() stage.

@return array
  A requirements array with the result of the charset check.
```

## Code

```php
function _system_check_db_utf8mb4_requirements($phase) {
  global $install_state;
  // In the requirements check of the installer, skip the utf8mb4 check unless
  // the database connection info has been preconfigured by hand with valid
  // information before running the installer, as otherwise we cannot get a
  // valid database connection object.
  if (isset($install_state['settings_verified']) && !$install_state['settings_verified']) {
    return array();
  }

  $connection = Database::getConnection();
  $t = get_t();
  $requirements['title'] = $t('Database 4 byte UTF-8 support');

  $utf8mb4_configurable = $connection->utf8mb4IsConfigurable();
  $utf8mb4_active = $connection->utf8mb4IsActive();
  $utf8mb4_supported = $connection->utf8mb4IsSupported();
  $driver = $connection->driver();
  $documentation_url = 'https://www.drupal.org/node/2754539';

  if ($utf8mb4_active) {
    if ($utf8mb4_supported) {
      if ($phase != 'install' && $utf8mb4_configurable && !variable_get('drupal_all_databases_are_utf8mb4', FALSE)) {
        // Supported, active, and configurable, but not all database tables
        // have been converted yet.
        $requirements['value'] = $t('Enabled, but database tables need conversion');
        $requirements['description'] = $t('Please convert all database tables to utf8mb4 prior to enabling it in settings.php. See the <a href="@url">documentation on adding 4 byte UTF-8 support</a> for more information.', array('@url' => $documentation_url));
        $requirements['severity'] = REQUIREMENT_ERROR;
      }
      else {
        // Supported, active.
        $requirements['value'] = $t('Enabled');
        $requirements['description'] = $t('4 byte UTF-8 for @driver is enabled.', array('@driver' => $driver));
        $requirements['severity'] = REQUIREMENT_OK;
      }
    }
    else {
      // Not supported, active.
      $requirements['value'] = $t('Not supported');
      $requirements['description'] = $t('4 byte UTF-8 for @driver is activated, but not supported on your system. Please turn this off in settings.php, or ensure that all database-related requirements are met. See the <a href="@url">documentation on adding 4 byte UTF-8 support</a> for more information.', array('@driver' => $driver, '@url' => $documentation_url));
      $requirements['severity'] = REQUIREMENT_ERROR;
    }
  }
  else {
    if ($utf8mb4_supported) {
      // Supported, not active.
      $requirements['value'] = $t('Not enabled');
      $requirements['description'] = $t('4 byte UTF-8 for @driver is not activated, but it is supported on your system. It is recommended that you enable this to allow 4-byte UTF-8 input such as emojis, Asian symbols and mathematical symbols to be stored correctly. See the <a href="@url">documentation on adding 4 byte UTF-8 support</a> for more information.', array('@driver' => $driver, '@url' => $documentation_url));
      $requirements['severity'] = REQUIREMENT_INFO;
    }
    else {
      // Not supported, not active.
      $requirements['value'] = $t('Disabled');
      $requirements['description'] = $t('4 byte UTF-8 for @driver is disabled. See the <a href="@url">documentation on adding 4 byte UTF-8 support</a> for more information.', array('@driver' => $driver, '@url' => $documentation_url));
      $requirements['severity'] = REQUIREMENT_INFO;
    }
  }
  return $requirements;
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
