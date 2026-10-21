# node_access_test_node_delete()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 202–204 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L202-L204)
- **Module/theme:** node_test
- **Implements:** [hook_node_delete()](../../node.api.php/hook_node_delete.md)

## Signature

```php
function node_access_test_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function node_access_test_node_delete($node) {
  db_delete('node_access_test')->condition('nid', $node->nid)->execute();
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
