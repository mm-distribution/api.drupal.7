# node_test_entity_view_mode_alter()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 158–163 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L158-L163)
- **Module/theme:** node_test
- **Implements:** [hook_entity_view_mode_alter()](../../../system/system.api.php/hook_entity_view_mode_alter.md)

## Signature

```php
function node_test_entity_view_mode_alter(&$view_mode, $context)
```

## Documentation

```text
Implements hook_entity_view_mode_alter().
```

## Code

```php
function node_test_entity_view_mode_alter(&$view_mode, $context) {
  // Only alter the view mode if we are on the test callback.
  if ($change_view_mode = variable_get('node_test_change_view_mode', '')) {
    $view_mode = $change_view_mode;
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
