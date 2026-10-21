# hook_modules_disabled()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2716–2720 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2716-L2720)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_modules_disabled($modules)
```

## Documentation

```text
Perform necessary actions after modules are disabled.

This function differs from hook_disable() in that it gives all other modules
a chance to perform actions when modules are disabled, whereas hook_disable()
is only called on the module actually being disabled.

@param $modules
  An array of the modules that were disabled.

@see hook_disable()
@see hook_modules_uninstalled()
```

## Code

```php
function hook_modules_disabled($modules) {
  if (in_array('lousy_module', $modules)) {
    mymodule_enable_functionality();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_modules_disabled()".

- [module_test_modules_disabled()](../../simpletest/tests/module_test.module/module_test_modules_disabled.md) — `modules/simpletest/tests/module_test.module`
- [system_test_modules_disabled()](../../simpletest/tests/system_test.module/system_test_modules_disabled.md) — `modules/simpletest/tests/system_test.module`
- [field_modules_disabled()](../../field/field.module/field_modules_disabled.md) — `modules/field/field.module`
- [filter_modules_disabled()](../../filter/filter.module/filter_modules_disabled.md) — `modules/filter/filter.module`
- [locale_modules_disabled()](../../locale/locale.module/locale_modules_disabled.md) — `modules/locale/locale.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
