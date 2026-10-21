# NodePageCacheTest::testNodeDelete()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 3055–3093 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L3055-L3093)
- **Class:** [NodePageCacheTest](../NodePageCacheTest.md)
- **Module/theme:** node

## Signature

```php
public function testNodeDelete()
```

## Documentation

```text
Tests deleting nodes clears page cache.
```

## Code

```php
  public function testNodeDelete() {
    $node_path = 'node/' . $this->drupalCreateNode()->nid;

    // Populate page cache.
    $this->drupalGet($node_path);

    // Login and delete the node.
    $this->drupalLogin($this->admin_user);
    $this->drupalPost($node_path . '/delete', array(), t('Delete'));

    // Logout and check the node is not available.
    $this->drupalLogout();
    $this->drupalGet($node_path);
    $this->assertResponse(404);

    // Create two new nodes.
    $nodes[0] = $this->drupalCreateNode();
    $nodes[1] = $this->drupalCreateNode();
    $node_path = 'node/' . $nodes[0]->nid;

    // Populate page cache.
    $this->drupalGet($node_path);

    // Login and delete the nodes.
    $this->drupalLogin($this->admin_user);
    $this->drupalGet('admin/content');
    $edit = array(
        'operation' => 'delete',
        'nodes[' . $nodes[0]->nid . ']' => TRUE,
        'nodes[' . $nodes[1]->nid . ']' => TRUE,
    );
    $this->drupalPost(NULL, $edit, t('Update'));
    $this->drupalPost(NULL, array(), t('Delete'));

    // Logout and check the node is not available.
    $this->drupalLogout();
    $this->drupalGet($node_path);
    $this->assertResponse(404);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
