# hook_hook_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 37–45 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L37-L45)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_hook_info()
```

## Documentation

```text
Defines one or more hooks that are exposed by a module.

Normally hooks do not need to be explicitly defined. However, by declaring a
hook explicitly, a module may define a "group" for it. Modules that implement
a hook may then place their implementation in either $module.module or in
$module.$group.inc. If the hook is located in $module.$group.inc, then that
file will be automatically loaded when needed.
In general, hooks that are rarely invoked and/or are very large should be
placed in a separate include file, while hooks that are very short or very
frequently called should be left in the main module file so that they are
always available.

@return
  An associative array whose keys are hook names and whose values are an
  associative array containing:
  - group: A string defining the group to which the hook belongs. The module
    system will determine whether a file with the name $module.$group.inc
    exists, and automatically load it when required.

See system_hook_info() for all hook groups defined by Drupal core.

@see hook_hook_info_alter().
```

## Code

```php
function hook_hook_info() {
  $hooks['token_info'] = array(
    'group' => 'tokens',
  );
  $hooks['tokens'] = array(
    'group' => 'tokens',
  );
  return $hooks;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_hook_info()".

- [module_test_hook_info()](../../simpletest/tests/module_test.module/module_test_hook_info.md) — `modules/simpletest/tests/module_test.module`
- [system_hook_info()](../system.module/system_hook_info.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
