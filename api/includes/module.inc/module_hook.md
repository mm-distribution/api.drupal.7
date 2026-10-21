# module_hook()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 688–703 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L688-L703)
- **Topics:** [hooks](../../topics/hooks.md)

## Signature

```php
function module_hook($module, $hook)
```

## Documentation

```text
Determines whether a module implements a hook.

@param $module
  The name of the module (without the .module extension).
@param $hook
  The name of the hook (e.g. "help" or "menu").

@return
  TRUE if the module is both installed and enabled, and the hook is
  implemented in that module.
```

## Code

```php
function module_hook($module, $hook) {
  $function = $module . '_' . $hook;
  if (function_exists($function)) {
    return TRUE;
  }
  // If the hook implementation does not exist, check whether it may live in an
  // optional include file registered via hook_hook_info().
  $hook_info = module_hook_info();
  if (isset($hook_info[$hook]['group'])) {
    module_load_include('inc', $module, $module . '.' . $hook_info[$hook]['group']);
    if (function_exists($function)) {
      return TRUE;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
