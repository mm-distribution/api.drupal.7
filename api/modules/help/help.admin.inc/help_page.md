# help_page()

- **Type:** Function
- **File:** [`modules/help/help.admin.inc`](_file.md), lines 24–50 · [local source](../../../../source/modules/help/help.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.admin.inc#L24-L50)
- **Module/theme:** help

## Signature

```php
function help_page($name)
```

## Documentation

```text
Menu callback; prints a page listing general help for a module.

@param $name
  A module name to display a help page for.
```

## Code

```php
function help_page($name) {
  $output = '';
  if (module_hook($name, 'help')) {
    $info = system_get_info('module');
    drupal_set_title($info[$name]['name']);

    $temp = module_invoke($name, 'help', "admin/help#$name", drupal_help_arg());
    if (empty($temp)) {
      $output .= t("No help is available for module %module.", array('%module' => $info[$name]['name']));
    }
    else {
      $output .= $temp;
    }

    // Only print list of administration pages if the module in question has
    // any such pages associated to it.
    $admin_tasks = system_get_module_admin_tasks($name, $info[$name]);
    if (!empty($admin_tasks)) {
      $links = array();
      foreach ($admin_tasks as $task) {
        $links[] = l($task['title'], $task['link_path'], $task['localized_options']);
      }
      $output .= theme('item_list', array('items' => $links, 'title' => t('@module administration pages', array('@module' => $info[$name]['name']))));
    }
  }
  return $output;
}
```

---
_Drupal 7.103 · [modules/help/help.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/help/help.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
