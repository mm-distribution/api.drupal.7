# system_admin_index()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 80–106 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L80-L106)
- **Module/theme:** system

## Signature

```php
function system_admin_index()
```

## Documentation

```text
Menu callback; prints a listing of admin tasks, organized by module.
```

## Code

```php
function system_admin_index() {
  $module_info = system_get_info('module');
  foreach ($module_info as $module => $info) {
    $module_info[$module] = new stdClass();
    $module_info[$module]->info = $info;
  }
  uasort($module_info, 'system_sort_modules_by_info_name');
  $menu_items = array();

  foreach ($module_info as $module => $info) {
    // Only display a section if there are any available tasks.
    if ($admin_tasks = system_get_module_admin_tasks($module, $info->info)) {
      // Sort links by title.
      uasort($admin_tasks, 'drupal_sort_title');
      // Move 'Configure permissions' links to the bottom of each section.
      $permission_key = "admin/people/permissions#module-$module";
      if (isset($admin_tasks[$permission_key])) {
        $permission_task = $admin_tasks[$permission_key];
        unset($admin_tasks[$permission_key]);
        $admin_tasks[$permission_key] = $permission_task;
      }

      $menu_items[$info->info['name']] = array($info->info['description'], $admin_tasks);
    }
  }
  return theme('system_admin_index', array('menu_items' => $menu_items));
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
