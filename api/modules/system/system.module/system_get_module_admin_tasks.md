# system_get_module_admin_tasks()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2999–3072 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2999-L3072)
- **Module/theme:** system

## Signature

```php
function system_get_module_admin_tasks($module, $info)
```

## Documentation

```text
Generate a list of tasks offered by a specified module.

@param $module
  Module name.
@param $info
  The module's information, as provided by system_get_info().

@return
  An array of task links.
```

## Code

```php
function system_get_module_admin_tasks($module, $info) {
  $links = &drupal_static(__FUNCTION__);

  if (!isset($links)) {
    $links = array();
    $query = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC));
    $query->join('menu_router', 'm', 'm.path = ml.router_path');
    $query
      ->fields('ml')
      // Weight should be taken from {menu_links}, not {menu_router}.
      ->fields('m', array_diff(drupal_schema_fields_sql('menu_router'), array('weight')))
      ->condition('ml.link_path', 'admin/%', 'LIKE')
      ->condition('ml.hidden', 0, '>=')
      ->condition('ml.module', 'system')
      ->condition('m.number_parts', 1, '>')
      ->condition('m.page_callback', 'system_admin_menu_block_page', '<>');
    foreach ($query->execute() as $link) {
      _menu_link_translate($link);
      if ($link['access']) {
        $links[$link['router_path']] = $link;
      }
    }
  }

  $admin_tasks = array();
  $titles = array();
  if ($menu = module_invoke($module, 'menu')) {
    foreach ($menu as $path => $item) {
      if (isset($links[$path])) {
        $task = $links[$path];
        // The link description, either derived from 'description' in
        // hook_menu() or customized via menu module is used as title attribute.
        if (!empty($task['localized_options']['attributes']['title'])) {
          $task['description'] = $task['localized_options']['attributes']['title'];
          unset($task['localized_options']['attributes']['title']);
        }

        // Check the admin tasks for duplicate names. If one is found,
        // append the parent menu item's title to differentiate.
        $duplicate_path = array_search($task['title'], $titles);
        if ($duplicate_path !== FALSE) {
          if ($parent = menu_link_load($task['plid'])) {
            // Append the parent item's title to this task's title.
            $task['title'] = t('@original_title (@parent_title)', array('@original_title' => $task['title'], '@parent_title' => $parent['title']));
          }
          if ($parent = menu_link_load($admin_tasks[$duplicate_path]['plid'])) {
            // Append the parent item's title to the duplicated task's title.
            // We use $links[$duplicate_path] in case there are triplicates.
            $admin_tasks[$duplicate_path]['title'] = t('@original_title (@parent_title)', array('@original_title' => $links[$duplicate_path]['title'], '@parent_title' => $parent['title']));
          }
        }
        else {
          $titles[$path] = $task['title'];
        }

        $admin_tasks[$path] = $task;
      }
    }
  }

  // Append link for permissions.
  if (module_hook($module, 'permission')) {
    $item = menu_get_item('admin/people/permissions');
    if (!empty($item['access'])) {
      $item['link_path'] = $item['href'];
      $item['title'] = t('Configure @module permissions', array('@module' => $info['name']));
      unset($item['description']);
      $item['localized_options']['fragment'] = 'module-' . $module;
      $admin_tasks["admin/people/permissions#module-$module"] = $item;
    }
  }

  return $admin_tasks;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
