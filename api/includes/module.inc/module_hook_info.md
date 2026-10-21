# module_hook_info()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 851–892 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L851-L892)
- **Topics:** [hooks](../../topics/hooks.md)

## Signature

```php
function module_hook_info()
```

## Documentation

```text
Retrieves a list of hooks that are declared through hook_hook_info().

@return
  An associative array whose keys are hook names and whose values are an
  associative array containing a group name. The structure of the array
  is the same as the return value of hook_hook_info().

@see hook_hook_info()
```

## Code

```php
function module_hook_info() {
  // This function is indirectly invoked from bootstrap_invoke_all(), in which
  // case common.inc, subsystems, and modules are not loaded yet, so it does not
  // make sense to support hook groups resp. lazy-loaded include files prior to
  // full bootstrap.
  if (drupal_bootstrap(NULL, FALSE) != DRUPAL_BOOTSTRAP_FULL) {
    return array();
  }
  $hook_info = &drupal_static(__FUNCTION__);

  if (!isset($hook_info)) {
    $hook_info = array();
    $cache = cache_get('hook_info', 'cache_bootstrap');
    if ($cache === FALSE) {
      // Rebuild the cache and save it.
      // We can't use module_invoke_all() here or it would cause an infinite
      // loop.
      foreach (module_list() as $module) {
        $function = $module . '_hook_info';
        if (function_exists($function)) {
          $result = $function();
          if (isset($result) && is_array($result)) {
            $hook_info = array_merge_recursive($hook_info, $result);
          }
        }
      }
      // We can't use drupal_alter() for the same reason as above.
      foreach (module_list() as $module) {
        $function = $module . '_hook_info_alter';
        if (function_exists($function)) {
          $function($hook_info);
        }
      }
      cache_set('hook_info', $hook_info, 'cache_bootstrap');
    }
    else {
      $hook_info = $cache->data;
    }
  }

  return $hook_info;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
