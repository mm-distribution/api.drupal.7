# system_test_modules_uninstalled()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 307–313 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L307-L313)
- **Module/theme:** batch_test
- **Implements:** [hook_modules_uninstalled()](../../../system/system.api.php/hook_modules_uninstalled.md)

## Signature

```php
function system_test_modules_uninstalled($modules)
```

## Documentation

```text
Implements hook_modules_uninstalled().
```

## Code

```php
function system_test_modules_uninstalled($modules) {
  if (variable_get('test_verbose_module_hooks')) {
    foreach ($modules as $module) {
      drupal_set_message(t('hook_modules_uninstalled fired for @module', array('@module' => $module)));
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
