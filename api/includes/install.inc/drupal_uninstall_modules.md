# drupal_uninstall_modules()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 774–822 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L774-L822)

## Signature

```php
function drupal_uninstall_modules($module_list = array(), $uninstall_dependents = TRUE)
```

## Documentation

```text
Uninstalls a given list of disabled modules.

@param string[] $module_list
  The modules to uninstall. It is the caller's responsibility to ensure that
  all modules in this list have already been disabled before this function
  is called.
@param bool $uninstall_dependents
  (optional) If TRUE, the function will check that all modules which depend
  on the passed-in module list either are already uninstalled or contained in
  the list, and it will ensure that the modules are uninstalled in the
  correct order. This incurs a significant performance cost, so use FALSE if
  you know $module_list is already complete and in the correct order.
  Defaults to TRUE.

@return bool
  Returns TRUE if the operation succeeds or FALSE if it aborts due to an
  unsafe condition, namely, $uninstall_dependents is TRUE and a module in
  $module_list has dependents which are not already uninstalled and not also
  included in $module_list).

@see module_disable()
@see module_enable()
```

## Code

```php
function drupal_uninstall_modules($module_list = array(), $uninstall_dependents = TRUE) {
  if ($uninstall_dependents) {
    // Get all module data so we can find dependents and sort.
    $module_data = system_rebuild_module_data();
    // Create an associative array with weights as values.
    $module_list = array_flip(array_values($module_list));

    $profile = drupal_get_profile();
    foreach (array_keys($module_list) as $module) {
      if (!isset($module_data[$module]) || drupal_get_installed_schema_version($module) == SCHEMA_UNINSTALLED) {
        // This module doesn't exist or is already uninstalled. Skip it.
        unset($module_list[$module]);
        continue;
      }
      $module_list[$module] = $module_data[$module]->sort;

      // If the module has any dependents which are not already uninstalled and
      // not included in the passed-in list, abort. It is not safe to uninstall
      // them automatically because uninstalling a module is a destructive
      // operation.
      foreach (array_keys($module_data[$module]->required_by) as $dependent) {
        if (!isset($module_list[$dependent]) && drupal_get_installed_schema_version($dependent) != SCHEMA_UNINSTALLED && $dependent != $profile) {
          return FALSE;
        }
      }
    }

    // Sort the module list by pre-calculated weights.
    asort($module_list);
    $module_list = array_keys($module_list);
  }

  foreach ($module_list as $module) {
    // Uninstall the module.
    module_load_install($module);
    module_invoke($module, 'uninstall');
    drupal_uninstall_schema($module);

    watchdog('system', '%module module uninstalled.', array('%module' => $module), WATCHDOG_INFO);
    drupal_set_installed_schema_version($module, SCHEMA_UNINSTALLED);
  }

  if (!empty($module_list)) {
    // Let other modules react.
    module_invoke_all('modules_uninstalled', $module_list);
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
