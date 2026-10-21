# module_test_modules_uninstalled()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 127–131 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L127-L131)
- **Module/theme:** batch_test
- **Implements:** [hook_modules_uninstalled()](../../../system/system.api.php/hook_modules_uninstalled.md)

## Signature

```php
function module_test_modules_uninstalled($modules)
```

## Documentation

```text
Implements hook_modules_uninstalled().
```

## Code

```php
function module_test_modules_uninstalled($modules) {
  // Record the ordered list of modules that were passed in to this hook so we
  // can check that the modules were uninstalled in the correct sequence.
  variable_set('test_module_uninstall_order', $modules);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
