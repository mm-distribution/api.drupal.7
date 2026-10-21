# module_test_permission()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 6–10 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L6-L10)
- **Module/theme:** batch_test
- **Implements:** [hook_permission()](../../../system/system.api.php/hook_permission.md)

## Signature

```php
function module_test_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function module_test_permission() {
  return array(
    'module_test perm' => t('example perm for module_test module'),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
