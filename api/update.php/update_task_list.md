# update_task_list()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 321–332 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L321-L332)

## Signature

```php
function update_task_list($active = NULL)
```

## Documentation

```text
Adds the update task list to the current page.
```

## Code

```php
function update_task_list($active = NULL) {
  // Default list of tasks.
  $tasks = array(
    'requirements' => 'Verify requirements',
    'info' => 'Overview',
    'select' => 'Review updates',
    'run' => 'Run updates',
    'finished' => 'Review log',
  );

  drupal_add_region_content('sidebar_first', theme('task_list', array('items' => $tasks, 'active' => $active)));
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
