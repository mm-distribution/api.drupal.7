# system_test_modules_disabled()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 296–302 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L296-L302)
- **Module/theme:** batch_test
- **Implements:** [hook_modules_disabled()](../../../system/system.api.php/hook_modules_disabled.md)

## Signature

```php
function system_test_modules_disabled($modules)
```

## Documentation

```text
Implements hook_modules_disabled().
```

## Code

```php
function system_test_modules_disabled($modules) {
  if (variable_get('test_verbose_module_hooks')) {
    foreach ($modules as $module) {
      drupal_set_message(t('hook_modules_disabled fired for @module', array('@module' => $module)));
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
