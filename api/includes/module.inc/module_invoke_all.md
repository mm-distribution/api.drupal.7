# module_invoke_all()

- **Type:** Function
- **File:** [`includes/module.inc`](_file.md), lines 958–977 · [local source](../../../source/includes/module.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/module.inc#L958-L977)
- **Topics:** [hooks](../../topics/hooks.md)

## Signature

```php
function module_invoke_all($hook)
```

## Documentation

```text
Invokes a hook in all enabled modules that implement it.

All arguments are passed by value. Use drupal_alter() if you need to pass
arguments by reference.

@param $hook
  The name of the hook to invoke.
@param ...
  Arguments to pass to the hook.

@return
  An array of return values of the hook implementations. If modules return
  arrays from their implementations, those are merged into one array
  recursively. Note: integer keys in arrays will be lost, as the merge is
  done using array_merge_recursive().

@see drupal_alter()
```

## Code

```php
function module_invoke_all($hook) {
  $args = func_get_args();
  // Remove $hook from the arguments.
  unset($args[0]);
  $return = array();
  foreach (module_implements($hook) as $module) {
    $function = $module . '_' . $hook;
    if (function_exists($function)) {
      $result = call_user_func_array($function, $args);
      if (isset($result) && is_array($result)) {
        $return = array_merge_recursive($return, $result);
      }
      elseif (isset($result)) {
        $return[] = $result;
      }
    }
  }

  return $return;
}
```

---
_Drupal 7.103 · [includes/module.inc](https://github.com/drupal/drupal/blob/7.103/includes/module.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
