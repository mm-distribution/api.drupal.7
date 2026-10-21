# system_rebuild_module_data()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2483–2497 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2483-L2497)
- **Module/theme:** system

## Signature

```php
function system_rebuild_module_data()
```

## Documentation

```text
Rebuild, save, and return data about all currently available modules.

@return
  Array of all available modules and their data.
```

## Code

```php
function system_rebuild_module_data() {
  $modules_cache = &drupal_static(__FUNCTION__);
  // Only rebuild once per request. $modules and $modules_cache cannot be
  // combined into one variable, because the $modules_cache variable is reset by
  // reference from system_list_reset() during the rebuild.
  if (!isset($modules_cache)) {
    $modules = _system_rebuild_module_data();
    ksort($modules);
    system_get_files_database($modules, 'module');
    system_update_files_database($modules, 'module');
    $modules = _module_build_dependencies($modules);
    $modules_cache = $modules;
  }
  return $modules_cache;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
