# module_test_hook_dynamic_loading_invoke_all()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 101–104 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L101-L104)
- **Module/theme:** batch_test

## Signature

```php
function module_test_hook_dynamic_loading_invoke_all()
```

## Documentation

```text
Page callback for 'hook dynamic loading' test.

If the hook is dynamically loaded correctly, the menu callback should
return 'success!'.
```

## Code

```php
function module_test_hook_dynamic_loading_invoke_all() {
  $result = module_invoke_all('test_hook');
  return $result['module_test'];
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
