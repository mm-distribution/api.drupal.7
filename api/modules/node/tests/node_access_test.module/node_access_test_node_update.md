# node_access_test_node_update()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 216–218 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L216-L218)
- **Module/theme:** node_test
- **Implements:** [hook_node_update()](../../node.api.php/hook_node_update.md)

## Signature

```php
function node_access_test_node_update($node)
```

## Documentation

```text
Implements hook_node_update().
```

## Code

```php
function node_access_test_node_update($node) {
  _node_access_test_node_write($node);
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
