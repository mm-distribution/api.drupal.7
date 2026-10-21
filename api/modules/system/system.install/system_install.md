# system_install()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 666–698 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L666-L698)
- **Module/theme:** system
- **Implements:** [hook_install()](../system.api.php/hook_install.md)

## Signature

```php
function system_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function system_install() {
  // Create tables.
  drupal_install_schema('system');
  $versions = drupal_get_schema_versions('system');
  $version = $versions ? max($versions) : SCHEMA_INSTALLED;
  drupal_set_installed_schema_version('system', $version);

  // Clear out module list and hook implementation statics before calling
  // system_rebuild_theme_data().
  module_list(TRUE);
  module_implements('', FALSE, TRUE);

  // Ensure the schema versions are not based on a previous module list.
  drupal_static_reset('drupal_get_schema_versions');

  // Load system theme data appropriately.
  system_rebuild_theme_data();

  // Enable the default theme.
  variable_set('theme_default', 'bartik');
  db_update('system')
    ->fields(array('status' => 1))
    ->condition('type', 'theme')
    ->condition('name', 'bartik')
    ->execute();

  // Populate the cron key variable.
  $cron_key = drupal_random_key();
  variable_set('cron_key', $cron_key);

  // This variable indicates that the database is ready for hashed session ids.
  variable_set('hashed_session_ids_supported', TRUE);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
