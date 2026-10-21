# install_tasks_to_perform()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 492–508 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L492-L508)

## Signature

```php
function install_tasks_to_perform($install_state)
```

## Documentation

```text
Returns a list of tasks to perform during the current installation request.

Note that the list of tasks can change based on the installation state as
the page request evolves (for example, if an installation profile hasn't
been selected yet, we don't yet know which profile tasks need to be run).

You can override this using hook_install_tasks() or
hook_install_tasks_alter().

@param $install_state
  An array of information about the current installation state.

@return
  A list of tasks to be performed, with associated metadata as returned by
  hook_install_tasks().
```

## Code

```php
function install_tasks_to_perform($install_state) {
  // Start with a list of all currently available tasks.
  $tasks = install_tasks($install_state);
  foreach ($tasks as $name => $task) {
    // Remove any tasks that were already performed or that never should run.
    // Also, if we started this page request with an indication of the last
    // task that was completed, skip that task and all those that come before
    // it, unless they are marked as always needing to run.
    if ($task['run'] == INSTALL_TASK_SKIP || in_array($name, $install_state['tasks_performed']) || (!empty($install_state['completed_task']) && empty($completed_task_found) && $task['run'] != INSTALL_TASK_RUN_IF_REACHED)) {
      unset($tasks[$name]);
    }
    if (!empty($install_state['completed_task']) && $name == $install_state['completed_task']) {
      $completed_task_found = TRUE;
    }
  }
  return $tasks;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
