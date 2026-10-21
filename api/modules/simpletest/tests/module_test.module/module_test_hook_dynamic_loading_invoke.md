# module_test_hook_dynamic_loading_invoke()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 90–93 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L90-L93)
- **Module/theme:** batch_test

## Signature

```php
function module_test_hook_dynamic_loading_invoke()
```

## Documentation

```text
Page callback for 'hook dynamic loading' test.

If the hook is dynamically loaded correctly, the menu callback should
return 'success!'.
```

## Code

```php
function module_test_hook_dynamic_loading_invoke() {
  $result = module_invoke('module_test', 'test_hook');
  return $result['module_test'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
