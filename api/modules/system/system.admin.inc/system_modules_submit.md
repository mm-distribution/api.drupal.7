# system_modules_submit()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1117–1248 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1117-L1248)
- **Module/theme:** system

## Signature

```php
function system_modules_submit($form, &$form_state)
```

## Documentation

```text
Submit callback; handles modules form submission.
```

## Code

```php
function system_modules_submit($form, &$form_state) {
  include_once DRUPAL_ROOT . '/includes/install.inc';

  // Builds list of modules.
  $modules = array();
  // If we're not coming from the confirmation form, build the list of modules.
  if (empty($form_state['storage'])) {
    // If we're not coming from the confirmation form, build the module list.
    foreach ($form_state['values']['modules'] as $group_name => $group) {
      foreach ($group as $module => $enabled) {
        $modules[$module] = array('group' => $group_name, 'enabled' => $enabled['enable']);
      }
    }
  }
  else {
    // If we are coming from the confirmation form, fetch
    // the modules out of $form_state.
    $modules = $form_state['storage']['modules'];
  }

  // Collect data for all modules to be able to determine dependencies.
  $files = system_rebuild_module_data();

  // Sorts modules by weight.
  $sort = array();
  foreach (array_keys($modules) as $module) {
    $sort[$module] = $files[$module]->sort;
  }
  array_multisort($sort, $modules);

  // Makes sure all required modules are set to be enabled.
  $more_required = array();
  $missing_modules = array();
  foreach ($modules as $name => $module) {
    if ($module['enabled']) {
      // Checks that all dependencies are set to be enabled.  Stores the ones
      // that are not in $dependencies variable so that the user can be alerted
      // in the confirmation form that more modules need to be enabled.
      $dependencies = array();
      foreach (array_keys($files[$name]->requires) as $required) {
        if (empty($modules[$required]['enabled'])) {
          if (isset($files[$required])) {
            $dependencies[] = $files[$required]->info['name'];
            $modules[$required]['enabled'] = TRUE;
          }
          else {
            $missing_modules[$required]['depends'][] = $name;
            $modules[$name]['enabled'] = FALSE;
          }
        }
      }

      // Stores additional modules that need to be enabled in $more_required.
      if (!empty($dependencies)) {
        $more_required[$name] = array(
          'name' => $files[$name]->info['name'],
          'requires' => $dependencies,
        );
      }
    }
  }

  // Redirects to confirmation form if more modules need to be enabled.
  if ((!empty($more_required) || !empty($missing_modules)) && !isset($form_state['values']['confirm'])) {
    $form_state['storage'] = array(
      'more_required' => $more_required,
      'modules' => $modules,
      'missing_modules' => $missing_modules,
    );
    $form_state['rebuild'] = TRUE;
    return;
  }

  // Invokes hook_requirements('install').  If failures are detected, makes sure
  // the dependent modules aren't installed either.
  foreach ($modules as $name => $module) {
    // Only invoke hook_requirements() on modules that are going to be installed.
    if ($module['enabled'] && drupal_get_installed_schema_version($name) == SCHEMA_UNINSTALLED) {
      if (!drupal_check_module($name)) {
        $modules[$name]['enabled'] = FALSE;
        foreach (array_keys($files[$name]->required_by) as $required_by) {
          $modules[$required_by]['enabled'] = FALSE;
        }
      }
    }
  }

  // Initializes array of actions.
  $actions = array(
    'enable' => array(),
    'disable' => array(),
    'install' => array(),
  );

  // Builds arrays of modules that need to be enabled, disabled, and installed.
  foreach ($modules as $name => $module) {
    if ($module['enabled']) {
      if (drupal_get_installed_schema_version($name) == SCHEMA_UNINSTALLED) {
        $actions['install'][] = $name;
        $actions['enable'][] = $name;
      }
      elseif (!module_exists($name)) {
        $actions['enable'][] = $name;
      }
    }
    elseif (module_exists($name)) {
      $actions['disable'][] = $name;
    }
  }

  // Gets list of modules prior to install process, unsets $form_state['storage']
  // so we don't get redirected back to the confirmation form.
  $pre_install_list = module_list();
  unset($form_state['storage']);

  // Reverse the 'enable' list, to order dependencies before dependents.
  krsort($actions['enable']);

  // Installs, enables, and disables modules.
  module_enable($actions['enable'], FALSE);
  module_disable($actions['disable'], FALSE);

  // Gets module list after install process, flushes caches and displays a
  // message if there are changes.
  $post_install_list = module_list(TRUE);
  if ($pre_install_list != $post_install_list) {
    drupal_flush_all_caches();
    drupal_set_message(t('The configuration options have been saved.'));
  }

  $form_state['redirect'] = 'admin/modules';
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
