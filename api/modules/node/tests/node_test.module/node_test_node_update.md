# node_test_node_update()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 146–153 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L146-L153)
- **Module/theme:** node_test
- **Implements:** [hook_node_update()](../../node.api.php/hook_node_update.md)

## Signature

```php
function node_test_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function node_test_node_update($node) {
  // Determine changes on update.
  if (!empty($node->original) && $node->original->title == 'test_changes') {
    if ($node->original->title != $node->title) {
      $node->title .= '_update';
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
