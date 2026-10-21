# hook_modules_uninstalled()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2738–2745 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2738-L2745)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_modules_uninstalled($modules)
```

## Documentation

```text
Perform necessary actions after modules are uninstalled.

This function differs from hook_uninstall() in that it gives all other
modules a chance to perform actions when a module is uninstalled, whereas
hook_uninstall() is only called on the module actually being uninstalled.

It is recommended that you implement this hook if your module stores
data that may have been set by other modules.

@param $modules
  An array of the modules that were uninstalled.

@see hook_uninstall()
@see hook_modules_disabled()
```

## Code

```php
function hook_modules_uninstalled($modules) {
  foreach ($modules as $module) {
    db_delete('mymodule_table')
      ->condition('module', $module)
      ->execute();
  }
  mymodule_cache_rebuild();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_modules_uninstalled()".

- [module_test_modules_uninstalled()](../../simpletest/tests/module_test.module/module_test_modules_uninstalled.md) — `modules/simpletest/tests/module_test.module`
- [system_test_modules_uninstalled()](../../simpletest/tests/system_test.module/system_test_modules_uninstalled.md) — `modules/simpletest/tests/system_test.module`
- [block_modules_uninstalled()](../../block/block.module/block_modules_uninstalled.md) — `modules/block/block.module`
- [node_modules_uninstalled()](../../node/node.module/node_modules_uninstalled.md) — `modules/node/node.module`
- [rdf_modules_uninstalled()](../../rdf/rdf.module/rdf_modules_uninstalled.md) — `modules/rdf/rdf.module`
- [user_modules_uninstalled()](../../user/user.module/user_modules_uninstalled.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
