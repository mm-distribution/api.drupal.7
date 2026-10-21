# EntityLoadTestCase::testEntityLoadConditions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud.test`](../_file.md), lines 25–48 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test#L25-L48)
- **Class:** [EntityLoadTestCase](../EntityLoadTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testEntityLoadConditions()
```

## Documentation

```text
Tests the functionality for loading entities matching certain conditions.
```

## Code

```php
  public function testEntityLoadConditions() {
    // Create a few nodes. One of them is given an edge-case title of "Array",
    // because loading entities by an array of conditions is subject to PHP
    // array-to-string conversion issues and we want to test those.
    $node_1 = $this->drupalCreateNode(array('title' => 'Array'));
    $node_2 = $this->drupalCreateNode(array('title' => 'Node 2'));
    $node_3 = $this->drupalCreateNode(array('title' => 'Node 3'));

    // Load all entities so that they are statically cached.
    $all_nodes = entity_load('node', FALSE);

    // Check that the first node can be loaded by title.
    $nodes_loaded = entity_load('node', FALSE, array('title' => 'Array'));
    $this->assertEqual(array_keys($nodes_loaded), array($node_1->nid));

    // Check that the second and third nodes can be loaded by title using an
    // array of conditions, and that the first node is not loaded from the
    // cache along with them.
    $nodes_loaded = entity_load('node', FALSE, array('title' => array('Node 2', 'Node 3')));
    ksort($nodes_loaded);
    $this->assertEqual(array_keys($nodes_loaded), array($node_2->nid, $node_3->nid));
    $this->assertIdentical($nodes_loaded[$node_2->nid], $all_nodes[$node_2->nid], 'Loaded node 2 is identical to cached node.');
    $this->assertIdentical($nodes_loaded[$node_3->nid], $all_nodes[$node_3->nid], 'Loaded node 3 is identical to cached node.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test) · Licensed GPL-2.0-or-later (see LICENSE)._
