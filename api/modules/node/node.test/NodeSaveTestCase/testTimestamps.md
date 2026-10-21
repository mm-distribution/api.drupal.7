# NodeSaveTestCase::testTimestamps()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1377–1428 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1377-L1428)
- **Class:** [NodeSaveTestCase](../NodeSaveTestCase.md)
- **Module/theme:** node

## Signature

```php
function testTimestamps()
```

## Documentation

```text
Verifies accuracy of the "created" and "changed" timestamp functionality.
```

## Code

```php
  function testTimestamps() {
    // Use the default timestamps.
    $edit = array(
      'uid' => $this->web_user->uid,
      'type' => 'article',
      'title' => $this->randomName(8),
    );

    node_save((object) $edit);
    $node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertEqual($node->created, REQUEST_TIME, 'Creating a node sets default "created" timestamp.');
    $this->assertEqual($node->changed, REQUEST_TIME, 'Creating a node sets default "changed" timestamp.');

    // Store the timestamps.
    $created = $node->created;
    $changed = $node->changed;

    node_save($node);
    $node = $this->drupalGetNodeByTitle($edit['title'], TRUE);
    $this->assertEqual($node->created, $created, 'Updating a node preserves "created" timestamp.');

    // Programmatically set the timestamps using hook_node_presave.
    $node->title = 'testing_node_presave';

    node_save($node);
    $node = $this->drupalGetNodeByTitle('testing_node_presave', TRUE);
    $this->assertEqual($node->created, 280299600, 'Saving a node uses "created" timestamp set in presave hook.');
    $this->assertEqual($node->changed, 979534800, 'Saving a node uses "changed" timestamp set in presave hook.');

    // Programmatically set the timestamps on the node.
    $edit = array(
      'uid' => $this->web_user->uid,
      'type' => 'article',
      'title' => $this->randomName(8),
      'created' => 280299600, // Sun, 19 Nov 1978 05:00:00 GMT
      'changed' => 979534800, // Drupal 1.0 release.
    );

    node_save((object) $edit);
    $node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertEqual($node->created, 280299600, 'Creating a node uses user-set "created" timestamp.');
    $this->assertNotEqual($node->changed, 979534800, 'Creating a node doesn\'t use user-set "changed" timestamp.');

    // Update the timestamps.
    $node->created = 979534800;
    $node->changed = 280299600;

    node_save($node);
    $node = $this->drupalGetNodeByTitle($edit['title'], TRUE);
    $this->assertEqual($node->created, 979534800, 'Updating a node uses user-set "created" timestamp.');
    $this->assertNotEqual($node->changed, 280299600, 'Updating a node doesn\'t use user-set "changed" timestamp.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
