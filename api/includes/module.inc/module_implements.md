# module_implements()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 727–839 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L727-L839)
- **Topics:** [hooks](../../topics/hooks.md)

## Signature

```php
function module_implements($hook, $sort = FALSE, $reset = FALSE)
```

## Documentation

```text
Determines which modules are implementing a hook.

Lazy-loaded include files specified with "group" via hook_hook_info() or
hook_module_implements_alter() will be automatically included by this
function when necessary.

@param string $hook
  The name of the hook (e.g. "help" or "menu").
@param bool $sort
  By default, modules are ordered by weight and filename, settings this option
  to TRUE, module list will be ordered by module name.
@param bool $reset
  For internal use only: Whether to force the stored list of hook
  implementations to be regenerated (such as after enabling a new module,
  before processing hook_enable).

@return
  An array with the names of the modules which are implementing this hook.

@see module_implements_write_cache()
```

## Code

```php
function module_implements($hook, $sort = FALSE, $reset = FALSE) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['implementations'] = &drupal_static(__FUNCTION__);
    $drupal_static_fast['verified'] = &drupal_static(__FUNCTION__ . ':verified');
  }
  $implementations = &$drupal_static_fast['implementations'];
  $verified = &$drupal_static_fast['verified'];

  // We maintain a persistent cache of hook implementations in addition to the
  // static cache to avoid looping through every module and every hook on each
  // request. Benchmarks show that the benefit of this caching outweighs the
  // additional database hit even when using the default database caching
  // backend and only a small number of modules are enabled. The cost of the
  // cache_get() is more or less constant and reduced further when non-database
  // caching backends are used, so there will be more significant gains when a
  // large number of modules are installed or hooks invoked, since this can
  // quickly lead to module_hook() being called several thousand times
  // per request.
  if ($reset) {
    $implementations = array();
    $verified = array();
    cache_set('module_implements', array(), 'cache_bootstrap');
    drupal_static_reset('module_hook_info');
    drupal_static_reset('drupal_alter');
    cache_clear_all('hook_info', 'cache_bootstrap');
    cache_clear_all('system_cache_tables', 'cache');
    return;
  }

  // Fetch implementations from cache.
  // This happens on the first call to module_implements(*, *, FALSE) during a
  // request, but also when $implementations have been reset, e.g. after
  // module_enable().
  if (empty($implementations)) {
    $implementations = cache_get('module_implements', 'cache_bootstrap');
    if ($implementations === FALSE) {
      $implementations = array();
    }
    else {
      $implementations = $implementations->data;
    }
    // Forget all previously "verified" hooks, in case that $implementations
    // were cleared via drupal_static_reset('module_implements') instead of
    // module_implements(*, *, TRUE).
    $verified = array();
  }

  if (!isset($implementations[$hook])) {
    // The hook is not cached, so ensure that whether or not it has
    // implementations, that the cache is updated at the end of the request.
    $implementations['#write_cache'] = TRUE;
    // Discover implementations for this hook.
    $hook_info = module_hook_info();
    $implementations[$hook] = array();
    $list = module_list(FALSE, FALSE, $sort);
    foreach ($list as $module) {
      $include_file = isset($hook_info[$hook]['group']) && module_load_include('inc', $module, $module . '.' . $hook_info[$hook]['group']);
      // Since module_hook() may needlessly try to load the include file again,
      // function_exists() is used directly here.
      if (function_exists($module . '_' . $hook)) {
        $implementations[$hook][$module] = $include_file ? $hook_info[$hook]['group'] : FALSE;
      }
    }
    // Allow modules to change the weight of specific implementations, but avoid
    // an infinite loop.
    if ($hook != 'module_implements_alter') {
      // Remember the implementations before hook_module_implements_alter().
      $implementations_before = $implementations[$hook];
      drupal_alter('module_implements', $implementations[$hook], $hook);
      // Verify implementations that were added or modified.
      foreach (array_diff_assoc($implementations[$hook], $implementations_before) as $module => $group) {
        // If drupal_alter('module_implements') changed or added a $group, the
        // respective file needs to be included.
        if ($group) {
          module_load_include('inc', $module, "$module.$group");
        }
        // If a new implementation was added, verify that the function exists.
        if (!function_exists($module . '_' . $hook)) {
          unset($implementations[$hook][$module]);
        }
      }
    }
    // Implementations for this hook are now "verified".
    $verified[$hook] = TRUE;
  }
  elseif (!isset($verified[$hook])) {
    // Implementations for this hook were in the cache, but they are not
    // "verified" yet.
    foreach ($implementations[$hook] as $module => $group) {
      // If this hook implementation is stored in a lazy-loaded file, so include
      // that file first.
      if ($group) {
        module_load_include('inc', $module, "$module.$group");
      }
      // It is possible that a module removed a hook implementation without the
      // implementations cache being rebuilt yet, so we check whether the
      // function exists on each request to avoid undefined function errors.
      // Since module_hook() may needlessly try to load the include file again,
      // function_exists() is used directly here.
      if (!function_exists($module . '_' . $hook)) {
        // Clear out the stale implementation from the cache and force a cache
        // refresh to forget about no longer existing hook implementations.
        unset($implementations[$hook][$module]);
        $implementations['#write_cache'] = TRUE;
      }
    }
    $verified[$hook] = TRUE;
  }

  return array_keys($implementations[$hook]);
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
