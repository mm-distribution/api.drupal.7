# install_tasks()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 525–626 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L525-L626)

## Signature

```php
function install_tasks($install_state)
```

## Documentation

```text
Returns a list of all tasks the installer currently knows about.

This function will return tasks regardless of whether or not they are
intended to run on the current page request. However, the list can change
based on the installation state (for example, if an installation profile
hasn't been selected yet, we don't yet know which profile tasks will be
available).

@param $install_state
  An array of information about the current installation state.

@return
  A list of tasks, with associated metadata.
```

## Code

```php
function install_tasks($install_state) {
  // Determine whether translation import tasks will need to be performed.
  $needs_translations = count($install_state['locales']) > 1 && !empty($install_state['parameters']['locale']) && $install_state['parameters']['locale'] != 'en';

  // Start with the core installation tasks that run before handing control
  // to the installation profile.
  $tasks = array(
    'install_select_profile' => array(
      'display_name' => st('Choose profile'),
      'display' => count($install_state['profiles']) != 1,
      'run' => INSTALL_TASK_RUN_IF_REACHED,
    ),
    'install_select_locale' => array(
      'display_name' => st('Choose language'),
      'run' => INSTALL_TASK_RUN_IF_REACHED,
    ),
    'install_load_profile' => array(
      'run' => INSTALL_TASK_RUN_IF_REACHED,
    ),
    'install_verify_requirements' => array(
      'display_name' => st('Verify requirements'),
    ),
    'install_settings_form' => array(
      'display_name' => st('Set up database'),
      'type' => 'form',
      'run' => $install_state['settings_verified'] ? INSTALL_TASK_SKIP : INSTALL_TASK_RUN_IF_NOT_COMPLETED,
    ),
    'install_system_module' => array(
    ),
    'install_bootstrap_full' => array(
      'run' => INSTALL_TASK_RUN_IF_REACHED,
    ),
    'install_profile_modules' => array(
      'display_name' => count($install_state['profiles']) == 1 ? st('Install site') : st('Install profile'),
      'type' => 'batch',
    ),
    'install_import_locales' => array(
      'display_name' => st('Set up translations'),
      'display' => $needs_translations,
      'type' => 'batch',
      'run' => $needs_translations ? INSTALL_TASK_RUN_IF_NOT_COMPLETED : INSTALL_TASK_SKIP,
    ),
    'install_configure_form' => array(
      'display_name' => st('Configure site'),
      'type' => 'form',
    ),
  );

  // Now add any tasks defined by the installation profile.
  if (!empty($install_state['parameters']['profile'])) {
    // Load the profile install file, because it is not always loaded when
    // hook_install_tasks() is invoked (e.g. batch processing).
    $profile_install_file = DRUPAL_ROOT . '/profiles/' . $install_state['parameters']['profile'] . '/' . $install_state['parameters']['profile'] . '.install';
    if (file_exists($profile_install_file)) {
      include_once $profile_install_file;
    }
    $function = $install_state['parameters']['profile'] . '_install_tasks';
    if (function_exists($function)) {
      $result = $function($install_state);
      if (is_array($result)) {
        $tasks += $result;
      }
    }
  }

  // Finish by adding the remaining core tasks.
  $tasks += array(
    'install_import_locales_remaining' => array(
      'display_name' => st('Finish translations'),
      'display' => $needs_translations,
      'type' => 'batch',
      'run' => $needs_translations ? INSTALL_TASK_RUN_IF_NOT_COMPLETED : INSTALL_TASK_SKIP,
    ),
    'install_finished' => array(
      'display_name' => st('Finished'),
    ),
  );

  // Allow the installation profile to modify the full list of tasks.
  if (!empty($install_state['parameters']['profile'])) {
    $profile_file = DRUPAL_ROOT . '/profiles/' . $install_state['parameters']['profile'] . '/' . $install_state['parameters']['profile'] . '.profile';
    if (file_exists($profile_file)) {
      include_once $profile_file;
      $function = $install_state['parameters']['profile'] . '_install_tasks_alter';
      if (function_exists($function)) {
        $function($tasks, $install_state);
      }
    }
  }

  // Fill in default parameters for each task before returning the list.
  foreach ($tasks as $task_name => &$task) {
    $task += array(
      'display_name' => NULL,
      'display' => !empty($task['display_name']),
      'type' => 'normal',
      'run' => INSTALL_TASK_RUN_IF_NOT_COMPLETED,
      'function' => $task_name,
    );
  }
  return $tasks;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
