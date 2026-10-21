# common_test_module_implements_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 210–220 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L210-L220)
- **Module/theme:** batch_test
- **Implements:** [hook_module_implements_alter()](../../../system/system.api.php/hook_module_implements_alter.md)

## Signature

```php
function common_test_module_implements_alter(&$implementations, $hook)
```

## Documentation

```text
Implements hook_module_implements_alter().

@see block_drupal_alter_foo_alter()
```

## Code

```php
function common_test_module_implements_alter(&$implementations, $hook) {
  // For drupal_alter(array('drupal_alter', 'drupal_alter_foo'), ...), make the
  // block module implementations run after all the other modules. Note that
  // when drupal_alter() is called with an array of types, the first type is
  // considered primary and controls the module order.
  if ($hook == 'drupal_alter_alter' && isset($implementations['block'])) {
    $group = $implementations['block'];
    unset($implementations['block']);
    $implementations['block'] = $group;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
