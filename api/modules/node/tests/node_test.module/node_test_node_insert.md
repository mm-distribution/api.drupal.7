# node_test_node_insert()

- **Type:** Function
- **File:** [`modules/node/tests/node_test.module`](_file.md), lines 172–181 · [local source](../../../../../source/modules/node/tests/node_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module#L172-L181)
- **Module/theme:** node_test
- **Implements:** [hook_node_insert()](../../node.api.php/hook_node_insert.md)

## Signature

```php
function node_test_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().

This tests saving a node on node insert.

@see NodeSaveTest::testNodeSaveOnInsert()
```

## Code

```php
function node_test_node_insert($node) {
  // Set the node title to the node ID and save.
  if ($node->title == 'new') {
    $node->title = 'Node '. $node->nid;
    // Remove the is_new flag, so that the node is updated and not inserted
    // again.
    unset($node->is_new);
    node_save($node);
  }
}
```

---
_Drupal 7.103 · [modules/node/tests/node_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
