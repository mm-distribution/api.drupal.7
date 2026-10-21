# system_test_module_implements_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 609–622 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L609-L622)
- **Module/theme:** batch_test
- **Implements:** [hook_module_implements_alter()](../../../system/system.api.php/hook_module_implements_alter.md)

## Signature

```php
function system_test_module_implements_alter(&$implementations, $hook)
```

## Documentation

```text
Implements hook_module_implements_alter().
```

## Code

```php
function system_test_module_implements_alter(&$implementations, $hook) {
  // For BootstrapGetFilenameWebTestCase::testRecursiveRebuilds() to work
  // correctly, this module's hook_schema() implementation cannot be either the
  // first implementation (since that would trigger a potential recursive
  // rebuild before anything is in the drupal_get_schema() cache) or the last
  // implementation (since that would trigger a potential recursive rebuild
  // after the cache is already complete). So put it somewhere in the middle.
  if ($hook == 'schema') {
    $group = $implementations['system_test'];
    unset($implementations['system_test']);
    $count = count($implementations);
    $implementations = array_merge(array_slice($implementations, 0, (int) ($count / 2), TRUE), array('system_test' => $group), array_slice($implementations, (int) ($count / 2), NULL, TRUE));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
