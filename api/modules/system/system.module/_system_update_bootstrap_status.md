# _system_update_bootstrap_status()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2506–2524 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2506-L2524)
- **Module/theme:** system

## Signature

```php
function _system_update_bootstrap_status()
```

## Documentation

```text
Refresh bootstrap column in the system table.

This is called internally by module_enable/disable() to flag modules that
implement hooks used during bootstrap, such as hook_boot(). These modules
are loaded earlier to invoke the hooks.
```

## Code

```php
function _system_update_bootstrap_status() {
  $bootstrap_modules = array();
  foreach (bootstrap_hooks() as $hook) {
    foreach (module_implements($hook) as $module) {
      $bootstrap_modules[] = $module;
    }
  }
  $query = db_update('system')->fields(array('bootstrap' => 0));
  if ($bootstrap_modules) {
    db_update('system')
      ->fields(array('bootstrap' => 1))
      ->condition('name', $bootstrap_modules, 'IN')
      ->execute();
    $query->condition('name', $bootstrap_modules, 'NOT IN');
  }
  $query->execute();
  // Reset the cached list of bootstrap modules.
  system_list_reset();
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
