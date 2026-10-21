# NodeSaveTestCase::testDeterminingChanges()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1434–1458 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1434-L1458)
- **Class:** [NodeSaveTestCase](../NodeSaveTestCase.md)
- **Module/theme:** node

## Signature

```php
function testDeterminingChanges()
```

## Documentation

```text
Tests determing changes in hook_node_presave() and verifies the static node
load cache is cleared upon save.
```

## Code

```php
  function testDeterminingChanges() {
    // Initial creation.
    $node = (object) array(
      'uid' => $this->web_user->uid,
      'type' => 'article',
      'title' => 'test_changes',
    );
    node_save($node);

    // Update the node without applying changes.
    node_save($node);
    $this->assertEqual($node->title, 'test_changes', 'No changes have been determined.');

    // Apply changes.
    $node->title = 'updated';
    node_save($node);

    // The hook implementations node_test_node_presave() and
    // node_test_node_update() determine changes and change the title.
    $this->assertEqual($node->title, 'updated_presave_update', 'Changes have been determined.');

    // Test the static node load cache to be cleared.
    $node = node_load($node->nid);
    $this->assertEqual($node->title, 'updated_presave', 'Static cache has been cleared.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
