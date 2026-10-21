# NodeRevisionsTestCase::testNodeRevisionWithoutLogMessage()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 254–297 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L254-L297)
- **Class:** [NodeRevisionsTestCase](../NodeRevisionsTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeRevisionWithoutLogMessage()
```

## Documentation

```text
Checks that revisions are correctly saved without log messages.
```

## Code

```php
  function testNodeRevisionWithoutLogMessage() {
    // Create a node with an initial log message.
    $log = $this->randomName(10);
    $node = $this->drupalCreateNode(array('log' => $log));

    // Save over the same revision and explicitly provide an empty log message
    // (for example, to mimic the case of a node form submitted with no text in
    // the "log message" field), and check that the original log message is
    // preserved.
    $new_title = $this->randomName(10) . 'testNodeRevisionWithoutLogMessage1';
    $updated_node = (object) array(
      'nid' => $node->nid,
      'vid' => $node->vid,
      'uid' => $node->uid,
      'type' => $node->type,
      'title' => $new_title,
      'log' => '',
    );
    node_save($updated_node);
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($new_title, 'New node title appears on the page.');
    $node_revision = node_load($node->nid, NULL, TRUE);
    $this->assertEqual($node_revision->log, $log, 'After an existing node revision is re-saved without a log message, the original log message is preserved.');

    // Create another node with an initial log message.
    $node = $this->drupalCreateNode(array('log' => $log));

    // Save a new node revision without providing a log message, and check that
    // this revision has an empty log message.
    $new_title = $this->randomName(10) . 'testNodeRevisionWithoutLogMessage2';
    $updated_node = (object) array(
      'nid' => $node->nid,
      'vid' => $node->vid,
      'uid' => $node->uid,
      'type' => $node->type,
      'title' => $new_title,
      'revision' => 1,
    );
    node_save($updated_node);
    $this->drupalGet('node/' . $node->nid);
    $this->assertText($new_title, 'New node title appears on the page.');
    $node_revision = node_load($node->nid, NULL, TRUE);
    $this->assertTrue(empty($node_revision->log), 'After a new node revision is saved with an empty log message, the log message for the node is empty.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
