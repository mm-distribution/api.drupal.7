# NodeLoadMultipleTestCase::testNodeMultipleLoad()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 50–105 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L50-L105)
- **Class:** [NodeLoadMultipleTestCase](../NodeLoadMultipleTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeMultipleLoad()
```

## Documentation

```text
Create four nodes and ensure they're loaded correctly.
```

## Code

```php
  function testNodeMultipleLoad() {
    $node1 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $node2 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $node3 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 0));
    $node4 = $this->drupalCreateNode(array('type' => 'page', 'promote' => 0));

    // Confirm that promoted nodes appear in the default node listing.
    $this->drupalGet('node');
    $this->assertText($node1->title, 'Node title appears on the default listing.');
    $this->assertText($node2->title, 'Node title appears on the default listing.');
    $this->assertNoText($node3->title, 'Node title does not appear in the default listing.');
    $this->assertNoText($node4->title, 'Node title does not appear in the default listing.');

    // Load nodes with only a condition. Nodes 3 and 4 will be loaded.
    $nodes = node_load_multiple(NULL, array('promote' => 0));
    $this->assertEqual($node3->title, $nodes[$node3->nid]->title, 'Node was loaded.');
    $this->assertEqual($node4->title, $nodes[$node4->nid]->title, 'Node was loaded.');
    $count = count($nodes);
    $this->assertTrue($count == 2, format_string('@count nodes loaded.', array('@count' => $count)));

    // Load nodes by nid. Nodes 1, 2 and 4 will be loaded.
    $nodes = node_load_multiple(array(1, 2, 4));
    $count = count($nodes);
    $this->assertTrue(count($nodes) == 3, format_string('@count nodes loaded', array('@count' => $count)));
    $this->assertTrue(isset($nodes[$node1->nid]), 'Node is correctly keyed in the array');
    $this->assertTrue(isset($nodes[$node2->nid]), 'Node is correctly keyed in the array');
    $this->assertTrue(isset($nodes[$node4->nid]), 'Node is correctly keyed in the array');
    foreach ($nodes as $node) {
      $this->assertTrue(is_object($node), 'Node is an object');
    }

    // Load nodes by nid, where type = article. Nodes 1, 2 and 3 will be loaded.
    $nodes = node_load_multiple(array(1, 2, 3, 4), array('type' => 'article'));
    $count = count($nodes);
    $this->assertTrue($count == 3, format_string('@count nodes loaded', array('@count' => $count)));
    $this->assertEqual($nodes[$node1->nid]->title, $node1->title, 'Node successfully loaded.');
    $this->assertEqual($nodes[$node2->nid]->title, $node2->title, 'Node successfully loaded.');
    $this->assertEqual($nodes[$node3->nid]->title, $node3->title, 'Node successfully loaded.');
    $this->assertFalse(isset($nodes[$node4->nid]));

    // Now that all nodes have been loaded into the static cache, ensure that
    // they are loaded correctly again when a condition is passed.
    $nodes = node_load_multiple(array(1, 2, 3, 4), array('type' => 'article'));
    $count = count($nodes);
    $this->assertTrue($count == 3, format_string('@count nodes loaded.', array('@count' => $count)));
    $this->assertEqual($nodes[$node1->nid]->title, $node1->title, 'Node successfully loaded');
    $this->assertEqual($nodes[$node2->nid]->title, $node2->title, 'Node successfully loaded');
    $this->assertEqual($nodes[$node3->nid]->title, $node3->title, 'Node successfully loaded');
    $this->assertFalse(isset($nodes[$node4->nid]), 'Node was not loaded');

    // Load nodes by nid, where type = article and promote = 0.
    $nodes = node_load_multiple(array(1, 2, 3, 4), array('type' => 'article', 'promote' => 0));
    $count = count($nodes);
    $this->assertTrue($count == 1, format_string('@count node loaded', array('@count' => $count)));
    $this->assertEqual($nodes[$node3->nid]->title, $node3->title, 'Node successfully loaded.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
