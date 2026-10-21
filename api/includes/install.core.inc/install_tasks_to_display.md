# install_tasks_to_display()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 643–651 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L643-L651)

## Signature

```php
function install_tasks_to_display($install_state)
```

## Documentation

```text
Returns a list of tasks that should be displayed to the end user.

The output of this function is a list suitable for sending to
theme_task_list().

@param $install_state
  An array of information about the current installation state.

@return
  A list of tasks, with keys equal to the machine-readable task name and
  values equal to the name that should be displayed.

@see theme_task_list()
```

## Code

```php
function install_tasks_to_display($install_state) {
  $displayed_tasks = array();
  foreach (install_tasks($install_state) as $name => $task) {
    if ($task['display']) {
      $displayed_tasks[$name] = $task['display_name'];
    }
  }
  return $displayed_tasks;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
