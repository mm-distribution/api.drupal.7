# install_run_tasks()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 325–359 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L325-L359)

## Signature

```php
function install_run_tasks(&$install_state)
```

## Documentation

```text
Runs all tasks for the current installation request.

In the case of an interactive installation, all tasks will be attempted
until one is reached that has output which needs to be displayed to the
user, or until a page redirect is required. Otherwise, tasks will be
attempted until the installation is finished.

@param $install_state
  An array of information about the current installation state. This is
  passed along to each task, so it can be modified if necessary.

@return
  HTML output from the last completed task.
```

## Code

```php
function install_run_tasks(&$install_state) {
  do {
    // Obtain a list of tasks to perform. The list of tasks itself can be
    // dynamic (e.g., some might be defined by the installation profile,
    // which is not necessarily known until the earlier tasks have run),
    // so we regenerate the remaining tasks based on the installation state,
    // each time through the loop.
    $tasks_to_perform = install_tasks_to_perform($install_state);
    // Run the first task on the list.
    reset($tasks_to_perform);
    $task_name = key($tasks_to_perform);
    $task = array_shift($tasks_to_perform);
    $install_state['active_task'] = $task_name;
    $original_parameters = $install_state['parameters'];
    $output = install_run_task($task, $install_state);
    $install_state['parameters_changed'] = ($install_state['parameters'] != $original_parameters);
    // Store this task as having been performed during the current request,
    // and save it to the database as completed, if we need to and if the
    // database is in a state that allows us to do so. Also mark the
    // installation as 'done' when we have run out of tasks.
    if (!$install_state['task_not_complete']) {
      $install_state['tasks_performed'][] = $task_name;
      $install_state['installation_finished'] = empty($tasks_to_perform);
      if ($install_state['database_tables_exist'] && ($task['run'] == INSTALL_TASK_RUN_IF_NOT_COMPLETED || $install_state['installation_finished'])) {
        variable_set('install_task', $install_state['installation_finished'] ? 'done' : $task_name);
      }
    }
    // Stop when there are no tasks left. In the case of an interactive
    // installation, also stop if we have some output to send to the browser,
    // the URL parameters have changed, or an end to the page request was
    // specifically called for.
    $finished = empty($tasks_to_perform) || ($install_state['interactive'] && (isset($output) || $install_state['parameters_changed'] || $install_state['stop_page_request']));
  } while (!$finished);
  return $output;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
