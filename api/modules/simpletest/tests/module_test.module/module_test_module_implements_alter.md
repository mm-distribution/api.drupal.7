# module_test_module_implements_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/module_test.module`](_file.md), lines 136–142 · [local source](../../../../../source/modules/simpletest/tests/module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module#L136-L142)
- **Module/theme:** batch_test
- **Implements:** [hook_module_implements_alter()](../../../system/system.api.php/hook_module_implements_alter.md)

## Signature

```php
function module_test_module_implements_alter(&$implementations, $hook)
```

## Documentation

```text
Implements hook_module_implements_alter()
```

## Code

```php
function module_test_module_implements_alter(&$implementations, $hook) {
  if ($hook === 'altered_test_hook') {
    // Add a hook implementation, that will be found in
    // module_test.implementations.inc.
    $implementations['module_test'] = 'implementations';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
