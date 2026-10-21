# NodeRevisionsTestCase::testRevisions()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 218–249 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L218-L249)
- **Class:** [NodeRevisionsTestCase](../NodeRevisionsTestCase.md)
- **Module/theme:** node

## Signature

```php
function testRevisions()
```

## Documentation

```text
Checks node revision related operations.
```

## Code

```php
  function testRevisions() {
    $nodes = $this->nodes;
    $logs = $this->logs;

    // Get last node for simple checks.
    $node = $nodes[3];

    // Confirm the correct revision text appears on "view revisions" page.
    $this->drupalGet("node/$node->nid/revisions/$node->vid/view");
    $this->assertText($node->body[LANGUAGE_NONE][0]['value'], 'Correct text displays for version.');

    // Confirm the correct log message appears on "revisions overview" page.
    $this->drupalGet("node/$node->nid/revisions");
    foreach ($logs as $log) {
      $this->assertText($log, 'Log message found.');
    }

    // Confirm that revisions revert properly.
    $this->drupalPost("node/$node->nid/revisions/{$nodes[1]->vid}/revert", array(), t('Revert'));
    $this->assertRaw(t('@type %title has been reverted back to the revision from %revision-date.',
                        array('@type' => 'Basic page', '%title' => $nodes[1]->title,
                              '%revision-date' => format_date($nodes[1]->revision_timestamp))), 'Revision reverted.');
    $reverted_node = node_load($node->nid);
    $this->assertTrue(($nodes[1]->body[LANGUAGE_NONE][0]['value'] == $reverted_node->body[LANGUAGE_NONE][0]['value']), 'Node reverted correctly.');

    // Confirm revisions delete properly.
    $this->drupalPost("node/$node->nid/revisions/{$nodes[1]->vid}/delete", array(), t('Delete'));
    $this->assertRaw(t('Revision from %revision-date of @type %title has been deleted.',
                        array('%revision-date' => format_date($nodes[1]->revision_timestamp),
                              '@type' => 'Basic page', '%title' => $nodes[1]->title)), 'Revision deleted.');
    $this->assertTrue(db_query('SELECT COUNT(vid) FROM {node_revision} WHERE nid = :nid and vid = :vid', array(':nid' => $node->nid, ':vid' => $nodes[1]->vid))->fetchField() == 0, 'Revision not found.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
