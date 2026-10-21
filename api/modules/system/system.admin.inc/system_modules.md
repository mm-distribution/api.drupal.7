# system_modules()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 791–954 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L791-L954)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_modules($form, $form_state = array())
```

## Documentation

```text
Menu callback; provides module enable/disable interface.

The list of modules gets populated by module.info files, which contain each
module's name, description, and information about which modules it requires.
See drupal_parse_info_file() for information on module.info descriptors.

Dependency checking is performed to ensure that a module:
- can not be enabled if there are disabled modules it requires.
- can not be disabled if there are enabled modules which depend on it.

@param $form_state
  An associative array containing the current state of the form.

@return
  The form array.

@ingroup forms
@see theme_system_modules()
@see system_modules_submit()
```

## Code

```php
function system_modules($form, $form_state = array()) {
  // Get current list of modules.
  $files = system_rebuild_module_data();

  // Remove hidden modules from display list.
  $visible_files = $files;
  foreach ($visible_files as $filename => $file) {
    if (!empty($file->info['hidden'])) {
      unset($visible_files[$filename]);
    }
  }

  uasort($visible_files, 'system_sort_modules_by_info_name');

  // If the modules form was submitted, then system_modules_submit() runs first
  // and if there are unfilled required modules, then $form_state['storage'] is
  // filled, triggering a rebuild. In this case we need to display a
  // confirmation form.
  if (!empty($form_state['storage'])) {
    return system_modules_confirm_form($visible_files, $form_state['storage']);
  }

  $modules = array();
  $form['modules'] = array('#tree' => TRUE);

  // Used when checking if module implements a help page.
  $help_arg = module_exists('help') ? drupal_help_arg() : FALSE;

  // Used when displaying modules that are required by the installation profile.
  require_once DRUPAL_ROOT . '/includes/install.inc';
  $distribution_name = check_plain(drupal_install_profile_distribution_name());

  // Iterate through each of the modules.
  foreach ($visible_files as $filename => $module) {
    $extra = array();
    $extra['enabled'] = (bool) $module->status;
    if (!empty($module->info['required'] )) {
      $extra['disabled'] = TRUE;
      $extra['required_by'][] = $distribution_name . (!empty($module->info['explanation']) ? ' ('. $module->info['explanation'] .')' : '');
    }

    // If this module requires other modules, add them to the array.
    foreach ($module->requires as $requires => $v) {
      if (!isset($files[$requires])) {
        $extra['requires'][$requires] = t('@module (<span class="admin-missing">missing</span>)', array('@module' => drupal_ucfirst($requires)));
        $extra['disabled'] = TRUE;
      }
      // Only display visible modules.
      elseif (isset($visible_files[$requires])) {
        $requires_name = $files[$requires]->info['name'];
        // Disable this module if it is incompatible with the dependency's version.
        if ($incompatible_version = drupal_check_incompatibility($v, str_replace(DRUPAL_CORE_COMPATIBILITY . '-', '', (string) $files[$requires]->info['version']))) {
          $extra['requires'][$requires] = t('@module (<span class="admin-missing">incompatible with</span> version @version)', array(
            '@module' => $requires_name . $incompatible_version,
            '@version' => $files[$requires]->info['version'],
          ));
          $extra['disabled'] = TRUE;
        }
        // Disable this module if the dependency is incompatible with this
        // version of Drupal core.
        elseif ($files[$requires]->info['core'] != DRUPAL_CORE_COMPATIBILITY) {
          $extra['requires'][$requires] = t('@module (<span class="admin-missing">incompatible with</span> this version of Drupal core)', array(
            '@module' => $requires_name,
          ));
          $extra['disabled'] = TRUE;
        }
        elseif ($files[$requires]->status) {
          $extra['requires'][$requires] = t('@module (<span class="admin-enabled">enabled</span>)', array('@module' => $requires_name));
        }
        else {
          $extra['requires'][$requires] = t('@module (<span class="admin-disabled">disabled</span>)', array('@module' => $requires_name));
        }
      }
    }
    // Generate link for module's help page, if there is one.
    if ($help_arg && $module->status && in_array($filename, module_implements('help'))) {
      if (module_invoke($filename, 'help', "admin/help#$filename", $help_arg)) {
        $extra['links']['help'] = array(
          '#type' => 'link',
          '#title' => t('Help'),
          '#href' => "admin/help/$filename",
          '#options' => array('attributes' => array('class' =>  array('module-link', 'module-link-help'), 'title' => t('Help'))),
        );
      }
    }
    // Generate link for module's permission, if the user has access to it.
    if ($module->status && user_access('administer permissions') && in_array($filename, module_implements('permission'))) {
      $extra['links']['permissions'] = array(
        '#type' => 'link',
        '#title' => t('Permissions'),
        '#href' => 'admin/people/permissions',
        '#options' => array('fragment' => 'module-' . $filename, 'attributes' => array('class' => array('module-link', 'module-link-permissions'), 'title' => t('Configure permissions'))),
      );
    }
    // Generate link for module's configuration page, if the module provides
    // one.
    if ($module->status && isset($module->info['configure'])) {
      $configure_link = menu_get_item($module->info['configure']);
      if ($configure_link === FALSE) {
        watchdog('system', 'Module %module specifies an invalid path for configuration: %configure', array(
          '%module' => $module->info['name'],
          '%configure' => $module->info['configure'],
        ));
      }
      else if ($configure_link['access']) {
        $extra['links']['configure'] = array(
          '#type' => 'link',
          '#title' => t('Configure'),
          '#href' => $configure_link['href'],
          '#options' => array('attributes' => array('class' => array('module-link', 'module-link-configure'), 'title' => $configure_link['description'])),
        );
      }
    }

    // If this module is required by other modules, list those, and then make it
    // impossible to disable this one.
    foreach ($module->required_by as $required_by => $v) {
      // Hidden modules are unset already.
      if (isset($visible_files[$required_by])) {
        if ($files[$required_by]->status == 1 && $module->status == 1) {
          $extra['required_by'][] = t('@module (<span class="admin-enabled">enabled</span>)', array('@module' => $files[$required_by]->info['name']));
          $extra['disabled'] = TRUE;
        }
        else {
          $extra['required_by'][] = t('@module (<span class="admin-disabled">disabled</span>)', array('@module' => $files[$required_by]->info['name']));
        }
      }
    }
    $form['modules'][$module->info['package']][$filename] = _system_modules_build_row($module->info, $extra);
  }

  // Add basic information to the fieldsets.
  foreach (element_children($form['modules']) as $package) {
    $form['modules'][$package] += array(
      '#type' => 'fieldset',
      '#title' => t($package),
      '#collapsible' => TRUE,
      '#theme' => 'system_modules_fieldset',
      '#header' => array(
        array('data' => t('Enabled'), 'class' => array('checkbox')),
        t('Name'),
        t('Version'),
        t('Description'),
        array('data' => t('Operations'), 'colspan' => 3),
      ),
      // Ensure that the "Core" package fieldset comes first.
      '#weight' => $package == 'Core' ? -10 : NULL,
      // Hide this package unless we're running a test.
      '#access' => !($package == 'Only For Testing' && !drupal_valid_test_ua()),
    );
  }

  // Lastly, sort all fieldsets by title.
  uasort($form['modules'], 'element_sort_by_title');

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save configuration'),
  );
  $form['#action'] = url('admin/modules/list/confirm');

  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
