# drupal_install_system()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 728–748 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L728-L748)

## Signature

```php
function drupal_install_system()
```

## Documentation

```text
Installs the system module.

Separated from the installation of other modules so core system
functions can be made available while other modules are installed.
```

## Code

```php
function drupal_install_system() {
  $system_path = drupal_get_path('module', 'system');
  require_once DRUPAL_ROOT . '/' . $system_path . '/system.install';
  module_invoke('system', 'install');

  $system_versions = drupal_get_schema_versions('system');
  $system_version = $system_versions ? max($system_versions) : SCHEMA_INSTALLED;
  db_insert('system')
    ->fields(array('filename', 'name', 'type', 'owner', 'status', 'schema_version', 'bootstrap'))
    ->values(array(
        'filename' => $system_path . '/system.module',
        'name' => 'system',
        'type' => 'module',
        'owner' => '',
        'status' => 1,
        'schema_version' => $system_version,
        'bootstrap' => 0,
      ))
    ->execute();
  system_rebuild_module_data();
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
