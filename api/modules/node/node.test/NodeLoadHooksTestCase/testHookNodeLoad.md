# NodeLoadHooksTestCase::testHookNodeLoad()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 127–149 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L127-L149)
- **Class:** [NodeLoadHooksTestCase](../NodeLoadHooksTestCase.md)
- **Module/theme:** node

## Signature

```php
function testHookNodeLoad()
```

## Documentation

```text
Test that hook_node_load() is invoked correctly.
```

## Code

```php
  function testHookNodeLoad() {
    // Create some sample articles and pages.
    $node1 = $this->drupalCreateNode(array('type' => 'article', 'status' => NODE_PUBLISHED));
    $node2 = $this->drupalCreateNode(array('type' => 'article', 'status' => NODE_PUBLISHED));
    $node3 = $this->drupalCreateNode(array('type' => 'article', 'status' => NODE_NOT_PUBLISHED));
    $node4 = $this->drupalCreateNode(array('type' => 'page', 'status' => NODE_NOT_PUBLISHED));

    // Check that when a set of nodes that only contains articles is loaded,
    // the properties added to the node by node_test_load_node() correctly
    // reflect the expected values.
    $nodes = node_load_multiple(array(), array('status' => NODE_PUBLISHED));
    $loaded_node = end($nodes);
    $this->assertEqual($loaded_node->node_test_loaded_nids, array($node1->nid, $node2->nid), 'hook_node_load() received the correct list of node IDs the first time it was called.');
    $this->assertEqual($loaded_node->node_test_loaded_types, array('article'), 'hook_node_load() received the correct list of node types the first time it was called.');

    // Now, as part of the same page request, load a set of nodes that contain
    // both articles and pages, and make sure the parameters passed to
    // node_test_node_load() are correctly updated.
    $nodes = node_load_multiple(array(), array('status' => NODE_NOT_PUBLISHED));
    $loaded_node = end($nodes);
    $this->assertEqual($loaded_node->node_test_loaded_nids, array($node3->nid, $node4->nid), 'hook_node_load() received the correct list of node IDs the second time it was called.');
    $this->assertEqual($loaded_node->node_test_loaded_types, array('article', 'page'), 'hook_node_load() received the correct list of node types the second time it was called.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
