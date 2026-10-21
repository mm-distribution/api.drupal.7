# node_access_test_permission()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 71–73 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L71-L73)
- **Module/theme:** node_test
- **Implements:** [hook_permission()](../../../system/system.api.php/hook_permission.md)

## Signature

```php
function node_access_test_permission()
```

## Documentation

```text
Implements hook_permission().

Sets up permissions for this module.
```

## Code

```php
function node_access_test_permission() {
  return array('node test view' => array('title' => 'View content'));
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
