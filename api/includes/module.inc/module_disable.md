# module_disable()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 540–616 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L540-L616)

## Signature

```php
function module_disable($module_list, $disable_dependents = TRUE)
```

## Documentation

```text
Disables a given set of modules.

@param string[] $module_list
  An array of module names.
@param bool $disable_dependents
  If TRUE, dependent modules will automatically be added and disabled in the
  correct order. This incurs a significant performance cost, so use FALSE
  if you know $module_list is already complete and in the correct order.

@see drupal_uninstall_modules()
@see module_enable()
```

## Code

```php
function module_disable($module_list, $disable_dependents = TRUE) {
  if ($disable_dependents) {
    // Get all module data so we can find dependents and sort.
    $module_data = system_rebuild_module_data();
    // Create an associative array with weights as values.
    $module_list = array_flip(array_values($module_list));

    $profile = drupal_get_profile();
    // The array is iterated over manually (instead of using a foreach) because
    // modules may be added to the list within the loop and we need to process
    // them.
    while ($module = key($module_list)) {
      next($module_list);
      if (!isset($module_data[$module]) || !$module_data[$module]->status) {
        // This module doesn't exist or is already disabled, skip it.
        unset($module_list[$module]);
        continue;
      }
      $module_list[$module] = $module_data[$module]->sort;

      // Add dependent modules to the list, with a placeholder weight.
      // The new modules will be processed as the while loop continues.
      foreach ($module_data[$module]->required_by as $dependent => $dependent_data) {
        if (!isset($module_list[$dependent]) && $dependent != $profile) {
          $module_list[$dependent] = 0;
        }
      }
    }

    // Sort the module list by pre-calculated weights.
    asort($module_list);
    $module_list = array_keys($module_list);
  }

  $invoke_modules = array();

  foreach ($module_list as $module) {
    if (module_exists($module)) {
      // Check if node_access table needs rebuilding.
      if (!node_access_needs_rebuild() && module_hook($module, 'node_grants')) {
        node_access_needs_rebuild(TRUE);
      }

      module_load_install($module);
      module_invoke($module, 'disable');
      db_update('system')
        ->fields(array('status' => 0))
        ->condition('type', 'module')
        ->condition('name', $module)
        ->execute();
      $invoke_modules[] = $module;
      watchdog('system', '%module module disabled.', array('%module' => $module), WATCHDOG_INFO);
    }
  }

  if (!empty($invoke_modules)) {
    // Refresh the module list to exclude the disabled modules.
    system_list_reset();
    module_list(TRUE);
    module_implements('', FALSE, TRUE);
    entity_info_cache_clear();
    // Invoke hook_modules_disabled before disabling modules,
    // so we can still call module hooks to get information.
    module_invoke_all('modules_disabled', $invoke_modules);
    // Update the registry to remove the newly-disabled module.
    registry_update();
    _system_update_bootstrap_status();
    // Update the theme registry to remove the newly-disabled module.
    drupal_theme_rebuild();
  }

  // If there remains no more node_access module, rebuilding will be
  // straightforward, we can do it right now.
  if (node_access_needs_rebuild() && count(module_implements('node_grants')) == 0) {
    node_access_rebuild();
  }
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
