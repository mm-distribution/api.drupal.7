# install_profile_modules()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1407–1449 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1407-L1449)

## Signature

```php
function install_profile_modules(&$install_state)
```

## Documentation

```text
Installs required modules via a batch process.

@param $install_state
  An array of information about the current installation state.

@return
  The batch definition.
```

## Code

```php
function install_profile_modules(&$install_state) {
  $modules = variable_get('install_profile_modules', array());
  $files = system_rebuild_module_data();
  variable_del('install_profile_modules');

  // Always install required modules first. Respect the dependencies between
  // the modules.
  $required = array();
  $non_required = array();
  // Although the profile module is marked as required, it needs to go after
  // every dependency, including non-required ones. So clear its required
  // flag for now to allow it to install late.
  $files[$install_state['parameters']['profile']]->info['required'] = FALSE;
  // Add modules that other modules depend on.
  foreach ($modules as $module) {
    if ($files[$module]->requires) {
      $modules = array_merge($modules, array_keys($files[$module]->requires));
    }
  }
  $modules = array_unique($modules);
  foreach ($modules as $module) {
    if (!empty($files[$module]->info['required'])) {
      $required[$module] = $files[$module]->sort;
    }
    else {
      $non_required[$module] = $files[$module]->sort;
    }
  }
  arsort($required);
  arsort($non_required);

  $operations = array();
  foreach ($required + $non_required as $module => $weight) {
    $operations[] = array('_install_module_batch', array($module, $files[$module]->info['name']));
  }
  $batch = array(
    'operations' => $operations,
    'title' => st('Installing @drupal', array('@drupal' => drupal_install_profile_distribution_name())),
    'error_message' => st('The installation has encountered an error.'),
    'finished' => '_install_profile_modules_finished',
  );
  return $batch;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
