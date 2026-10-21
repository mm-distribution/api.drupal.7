# module_test_hook_info()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 60–65 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L60-L65)
- **Module/theme:** batch_test
- **Implements:** [hook_hook_info()](../../../system/system.api.php/hook_hook_info.md)

## Signature

```php
function module_test_hook_info()
```

## Documentation

```text
Implements hook_hook_info().
```

## Code

```php
function module_test_hook_info() {
  $hooks['test_hook'] = array(
    'group' => 'file',
  );
  return $hooks;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
