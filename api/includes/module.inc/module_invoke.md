# module_invoke()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 930–937 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L930-L937)
- **Topics:** [hooks](../../topics/hooks.md)

## Signature

```php
function module_invoke($module, $hook)
```

## Documentation

```text
Invokes a hook in a particular module.

All arguments are passed by value. Use drupal_alter() if you need to pass
arguments by reference.

@param $module
  The name of the module (without the .module extension).
@param $hook
  The name of the hook to invoke.
@param ...
  Arguments to pass to the hook implementation.

@return
  The return value of the hook implementation.

@see drupal_alter()
```

## Code

```php
function module_invoke($module, $hook) {
  $args = func_get_args();
  // Remove $module and $hook from the arguments.
  unset($args[0], $args[1]);
  if (module_hook($module, $hook)) {
    return call_user_func_array($module . '_' . $hook, $args);
  }
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
