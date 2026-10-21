# system_test_modules_enabled()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 285–291 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L285-L291)
- **Module/theme:** batch_test
- **Implements:** [hook_modules_enabled()](../../../system/system.api.php/hook_modules_enabled.md)

## Signature

```php
function system_test_modules_enabled($modules)
```

## Documentation

```text
Implements hook_modules_enabled().
```

## Code

```php
function system_test_modules_enabled($modules) {
  if (variable_get('test_verbose_module_hooks')) {
    foreach ($modules as $module) {
      drupal_set_message(t('hook_modules_enabled fired for @module', array('@module' => $module)));
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
