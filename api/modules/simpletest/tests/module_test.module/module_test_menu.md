# module_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 70–82 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L70-L82)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function module_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function module_test_menu() {
  $items['module-test/hook-dynamic-loading-invoke'] = array(
    'title' => 'Test hook dynamic loading (invoke)',
    'page callback' => 'module_test_hook_dynamic_loading_invoke',
    'access arguments' => array('access content'),
  );
  $items['module-test/hook-dynamic-loading-invoke-all'] = array(
    'title' => 'Test hook dynamic loading (invoke_all)',
    'page callback' => 'module_test_hook_dynamic_loading_invoke_all',
    'access arguments' => array('access content'),
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
