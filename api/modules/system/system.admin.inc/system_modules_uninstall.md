# system_modules_uninstall()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1265–1322 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1265-L1322)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_modules_uninstall($form, $form_state = NULL)
```

## Documentation

```text
Builds a form of currently disabled modules.

@ingroup forms
@see system_modules_uninstall_validate()
@see system_modules_uninstall_submit()
@param $form_state['values']
  Submitted form values.
@return
  A form array representing the currently disabled modules.
```

## Code

```php
function system_modules_uninstall($form, $form_state = NULL) {
  // Make sure the install API is available.
  include_once DRUPAL_ROOT . '/includes/install.inc';

  // Display the confirm form if any modules have been submitted.
  if (!empty($form_state['storage']) && $confirm_form = system_modules_uninstall_confirm_form($form_state['storage'])) {
    return $confirm_form;
  }

  // Get a list of disabled, installed modules.
  $all_modules = system_rebuild_module_data();
  $disabled_modules = array();
  foreach ($all_modules as $name => $module) {
    if (empty($module->status) && $module->schema_version > SCHEMA_UNINSTALLED) {
      $disabled_modules[$name] = $module;
    }
  }

  // Only build the rest of the form if there are any modules available to
  // uninstall.
  if (!empty($disabled_modules)) {
    $profile = drupal_get_profile();
    uasort($disabled_modules, 'system_sort_modules_by_info_name');
    $form['uninstall'] = array('#tree' => TRUE);
    foreach ($disabled_modules as $module) {
      $module_name = $module->info['name'] ? $module->info['name'] : $module->name;
      $form['modules'][$module->name]['#module_name'] = $module_name;
      $form['modules'][$module->name]['name']['#markup'] = $module_name;
      $form['modules'][$module->name]['description']['#markup'] = t($module->info['description']);
      $form['uninstall'][$module->name] = array(
        '#type' => 'checkbox',
        '#title' => t('Uninstall @module module', array('@module' => $module_name)),
        '#title_display' => 'invisible',
      );
      // All modules which depend on this one must be uninstalled first, before
      // we can allow this module to be uninstalled. (The installation profile
      // is excluded from this list.)
      foreach (array_keys($module->required_by) as $dependent) {
        if ($dependent != $profile && drupal_get_installed_schema_version($dependent) != SCHEMA_UNINSTALLED) {
          $dependent_name = isset($all_modules[$dependent]->info['name']) ? $all_modules[$dependent]->info['name'] : $dependent;
          $form['modules'][$module->name]['#required_by'][] = $dependent_name;
          $form['uninstall'][$module->name]['#disabled'] = TRUE;
        }
      }
    }
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Uninstall'),
    );
    $form['#action'] = url('admin/modules/uninstall/confirm');
  }
  else {
    $form['modules'] = array();
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
