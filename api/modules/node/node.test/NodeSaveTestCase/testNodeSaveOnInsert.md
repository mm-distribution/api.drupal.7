# NodeSaveTestCase::testNodeSaveOnInsert()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1469–1474 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1469-L1474)
- **Class:** [NodeSaveTestCase](../NodeSaveTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeSaveOnInsert()
```

## Documentation

```text
Tests saving a node on node insert.

This test ensures that a node has been fully saved when hook_node_insert()
is invoked, so that the node can be saved again in a hook implementation
without errors.

@see node_test_node_insert()
```

## Code

```php
  function testNodeSaveOnInsert() {
    // node_test_node_insert() triggers a save on insert if the title equals
    // 'new'.
    $node = $this->drupalCreateNode(array('title' => 'new'));
    $this->assertEqual($node->title, 'Node ' . $node->nid, 'Node saved on node insert.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
