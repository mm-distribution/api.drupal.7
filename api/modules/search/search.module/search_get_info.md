# search_get_info()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 254–273 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L254-L273)
- **Module/theme:** search

## Signature

```php
function search_get_info($all = FALSE)
```

## Documentation

```text
Returns information about available search modules.

@param $all
  If TRUE, information about all enabled modules implementing
  hook_search_info() will be returned. If FALSE (default), only modules that
  have been set to active on the search settings page will be returned.

@return
  Array of hook_search_info() return values, keyed by module name. The
  'title' and 'path' array elements will be set to defaults for each module
  if not supplied by hook_search_info(), and an additional array element of
  'module' will be added (set to the module name).
```

## Code

```php
function search_get_info($all = FALSE) {
  $search_hooks = &drupal_static(__FUNCTION__);

  if (!isset($search_hooks)) {
    foreach (module_implements('search_info') as $module) {
      $search_hooks[$module] = call_user_func($module . '_search_info');
      // Use module name as the default value.
      $search_hooks[$module] += array('title' => $module, 'path' => $module);
      // Include the module name itself in the array.
      $search_hooks[$module]['module'] = $module;
    }
  }

  if ($all) {
    return $search_hooks;
  }

  $active = variable_get('search_active_modules', array('node', 'user'));
  return array_intersect_key($search_hooks, array_flip($active));
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
