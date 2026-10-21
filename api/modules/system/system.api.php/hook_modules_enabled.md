# hook_modules_enabled()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2696–2701 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2696-L2701)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_modules_enabled($modules)
```

## Documentation

```text
Perform necessary actions after modules are enabled.

This function differs from hook_enable() in that it gives all other modules a
chance to perform actions when modules are enabled, whereas hook_enable() is
only called on the module actually being enabled. See module_enable() for a
detailed description of the order in which install and enable hooks are
invoked.

@param $modules
  An array of the modules that were enabled.

@see hook_enable()
@see hook_modules_installed()
@see module_enable()
```

## Code

```php
function hook_modules_enabled($modules) {
  if (in_array('lousy_module', $modules)) {
    drupal_set_message(t('mymodule is not compatible with lousy_module'), 'error');
    mymodule_disable_functionality();
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_modules_enabled()".

- [module_test_modules_enabled()](../../simpletest/tests/module_test.module/module_test_modules_enabled.md) — `modules/simpletest/tests/module_test.module`
- [system_test_modules_enabled()](../../simpletest/tests/system_test.module/system_test_modules_enabled.md) — `modules/simpletest/tests/system_test.module`
- [comment_modules_enabled()](../../comment/comment.install/comment_modules_enabled.md) — `modules/comment/comment.install`
- [field_modules_enabled()](../../field/field.module/field_modules_enabled.md) — `modules/field/field.module`
- [filter_modules_enabled()](../../filter/filter.module/filter_modules_enabled.md) — `modules/filter/filter.module`
- [locale_modules_enabled()](../../locale/locale.module/locale_modules_enabled.md) — `modules/locale/locale.module`
- [node_modules_enabled()](../../node/node.module/node_modules_enabled.md) — `modules/node/node.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
