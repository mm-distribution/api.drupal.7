# module_test_modules_disabled()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 118–122 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L118-L122)
- **Module/theme:** batch_test
- **Implements:** [hook_modules_disabled()](../../../system/system.api.php/hook_modules_disabled.md)

## Signature

```php
function module_test_modules_disabled($modules)
```

## Documentation

```text
Implements hook_modules_disabled().
```

## Code

```php
function module_test_modules_disabled($modules) {
  // Record the ordered list of modules that were passed in to this hook so we
  // can check that the modules were disabled in the correct sequence.
  variable_set('test_module_disable_order', $modules);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
