# module_test_modules_enabled()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 109–113 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L109-L113)
- **Module/theme:** batch_test
- **Implements:** [hook_modules_enabled()](../../../system/system.api.php/hook_modules_enabled.md)

## Signature

```php
function module_test_modules_enabled($modules)
```

## Documentation

```text
Implements hook_modules_enabled().
```

## Code

```php
function module_test_modules_enabled($modules) {
  // Record the ordered list of modules that were passed in to this hook so we
  // can check that the modules were enabled in the correct sequence.
  variable_set('test_module_enable_order', $modules);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
