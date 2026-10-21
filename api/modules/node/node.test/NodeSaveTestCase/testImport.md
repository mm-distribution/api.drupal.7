# NodeSaveTestCase::testImport()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1347–1372 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1347-L1372)
- **Class:** [NodeSaveTestCase](../NodeSaveTestCase.md)
- **Module/theme:** node

## Signature

```php
function testImport()
```

## Documentation

```text
Checks whether custom node IDs are saved properly during an import operation.

Workflow:
 - first create a piece of content
 - save the content
 - check if node exists
```

## Code

```php
  function testImport() {
    // Node ID must be a number that is not in the database.
    $max_nid = db_query('SELECT MAX(nid) FROM {node}')->fetchField();
    $test_nid = $max_nid + mt_rand(1000, 1000000);
    $title = $this->randomName(8);
    $node = array(
      'title' => $title,
      'body' => array(LANGUAGE_NONE => array(array('value' => $this->randomName(32)))),
      'uid' => $this->web_user->uid,
      'type' => 'article',
      'nid' => $test_nid,
      'is_new' => TRUE,
    );
    $node = node_submit((object) $node);

    // Verify that node_submit did not overwrite the user ID.
    $this->assertEqual($node->uid, $this->web_user->uid, 'Function node_submit() preserves user ID');

    node_save($node);
    // Test the import.
    $node_by_nid = node_load($test_nid);
    $this->assertTrue($node_by_nid, 'Node load by node ID.');

    $node_by_title = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($node_by_title, 'Node load by node title.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
