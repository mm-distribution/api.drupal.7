# theme_task_list()

- **Type:** Function
- **File:** [`includes/theme.maintenance.inc`](_file.md), lines 104–130 · [local source](../../../source/includes/theme.maintenance.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc#L104-L130)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_task_list($variables)
```

## Documentation

```text
Returns HTML for a list of maintenance tasks to perform.

@param $variables
  An associative array containing:
  - items: An associative array of maintenance tasks.
  - active: The key for the currently active maintenance task.

@ingroup themeable
```

## Code

```php
function theme_task_list($variables) {
  $items = $variables['items'];
  $active = $variables['active'];

  $done = isset($items[$active]) || $active == NULL;
  $output = '<h2 class="element-invisible">Installation tasks</h2>';
  $output .= '<ol class="task-list">';

  foreach ($items as $k => $item) {
    if ($active == $k) {
      $class = 'active';
      $status = '(' . t('active') . ')';
      $done = FALSE;
    }
    else {
      $class = $done ? 'done' : '';
      $status = $done ? '(' . t('done') . ')' : '';
    }
    $output .= '<li';
    $output .= ($class ? ' class="' . $class . '"' : '') . '>';
    $output .= $item;
    $output .= ($status ? '<span class="element-invisible">' . $status . '</span>' : '');
    $output .= '</li>';
  }
  $output .= '</ol>';
  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.maintenance.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.maintenance.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
