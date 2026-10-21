# module_enable()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 401–525 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L401-L525)

## Signature

```php
function module_enable($module_list, $enable_dependencies = TRUE)
```

## Documentation

```text
Enables or installs a given list of modules.

Definitions:
- "Enabling" is the process of activating a module for use by Drupal.
- "Disabling" is the process of deactivating a module.
- "Installing" is the process of enabling it for the first time or after it
  has been uninstalled.
- "Uninstalling" is the process of removing all traces of a module.

Order of events:
- Gather and add module dependencies to $module_list (if applicable).
- For each module that is being enabled:
  - Install module schema and update system registries and caches.
  - If the module is being enabled for the first time or had been
    uninstalled, invoke hook_install() and add it to the list of installed
    modules.
  - Invoke hook_enable().
- Invoke hook_modules_installed().
- Invoke hook_modules_enabled().

@param string[] $module_list
  An array of module names.
@param bool $enable_dependencies
  If TRUE, dependencies will automatically be added and enabled in the
  correct order. This incurs a significant performance cost, so use FALSE
  if you know $module_list is already complete and in the correct order.

@return bool
  FALSE if one or more dependencies are missing, TRUE otherwise.

@see hook_install()
@see hook_enable()
@see hook_modules_installed()
@see hook_modules_enabled()
@see module_disable()
@see drupal_uninstall_modules()
```

## Code

```php
function module_enable($module_list, $enable_dependencies = TRUE) {
  if ($enable_dependencies) {
    // Get all module data so we can find dependencies and sort.
    $module_data = system_rebuild_module_data();
    // Create an associative array with weights as values.
    $module_list = array_flip(array_values($module_list));

    // The array is iterated over manually (instead of using a foreach) because
    // modules may be added to the list within the loop and we need to process
    // them.
    while ($module = key($module_list)) {
      next($module_list);
      if (!isset($module_data[$module])) {
        // This module is not found in the filesystem, abort.
        return FALSE;
      }
      if ($module_data[$module]->status) {
        // Skip already enabled modules.
        unset($module_list[$module]);
        continue;
      }
      $module_list[$module] = $module_data[$module]->sort;

      // Add dependencies to the list, with a placeholder weight.
      // The new modules will be processed as the while loop continues.
      foreach (array_keys($module_data[$module]->requires) as $dependency) {
        if (!isset($module_list[$dependency])) {
          $module_list[$dependency] = 0;
        }
      }
    }

    if (!$module_list) {
      // Nothing to do. All modules already enabled.
      return TRUE;
    }

    // Sort the module list by pre-calculated weights.
    arsort($module_list);
    $module_list = array_keys($module_list);
  }

  // Required for module installation checks.
  include_once DRUPAL_ROOT . '/includes/install.inc';

  $modules_installed = array();
  $modules_enabled = array();
  foreach ($module_list as $module) {
    // Only process modules that are not already enabled.
    $existing = db_query("SELECT status FROM {system} WHERE type = :type AND name = :name", array(
      ':type' => 'module',
      ':name' => $module))
      ->fetchObject();
    if ($existing->status == 0) {
      // Load the module's code.
      drupal_load('module', $module);
      module_load_install($module);

      // Update the database and module list to reflect the new module. This
      // needs to be done first so that the module's hook implementations,
      // hook_schema() in particular, can be called while it is being
      // installed.
      db_update('system')
        ->fields(array('status' => 1))
        ->condition('type', 'module')
        ->condition('name', $module)
        ->execute();
      // Refresh the module list to include it.
      system_list_reset();
      module_list(TRUE);
      module_implements('', FALSE, TRUE);
      _system_update_bootstrap_status();
      // Update the registry to include it.
      registry_update();
      // Refresh the schema to include it.
      drupal_get_schema(NULL, TRUE);
      // Update the theme registry to include it.
      drupal_theme_rebuild();
      // Clear entity cache.
      entity_info_cache_clear();

      // Now install the module if necessary.
      if (drupal_get_installed_schema_version($module, TRUE) == SCHEMA_UNINSTALLED) {
        drupal_install_schema($module);

        // Set the schema version to the number of the last update provided
        // by the module.
        $versions = drupal_get_schema_versions($module);
        $version = $versions ? max($versions) : SCHEMA_INSTALLED;

        // If the module has no current updates, but has some that were
        // previously removed, set the version to the value of
        // hook_update_last_removed().
        if ($last_removed = module_invoke($module, 'update_last_removed')) {
          $version = max($version, $last_removed);
        }
        drupal_set_installed_schema_version($module, $version);
        // Allow the module to perform install tasks.
        module_invoke($module, 'install');
        // Record the fact that it was installed.
        $modules_installed[] = $module;
        watchdog('system', '%module module installed.', array('%module' => $module), WATCHDOG_INFO);
      }

      // Enable the module.
      module_invoke($module, 'enable');

      // Record the fact that it was enabled.
      $modules_enabled[] = $module;
      watchdog('system', '%module module enabled.', array('%module' => $module), WATCHDOG_INFO);
    }
  }

  // If any modules were newly installed, invoke hook_modules_installed().
  if (!empty($modules_installed)) {
    module_invoke_all('modules_installed', $modules_installed);
  }

  // If any modules were newly enabled, invoke hook_modules_enabled().
  if (!empty($modules_enabled)) {
    module_invoke_all('modules_enabled', $modules_enabled);
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
