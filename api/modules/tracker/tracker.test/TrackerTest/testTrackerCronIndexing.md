# TrackerTest::testTrackerCronIndexing()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 253–305 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L253-L305)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerCronIndexing()
```

## Documentation

```text
Tests that existing nodes are indexed by cron.
```

## Code

```php
  function testTrackerCronIndexing() {
    $this->drupalLogin($this->user);

    // Create 3 nodes.
    $edits = array();
    $nodes = array();
    for ($i = 1; $i <= 3; $i++) {
      $edits[$i] = array(
        'comment' => 2,
        'title' => $this->randomName(),
      );
      $nodes[$i] = $this->drupalCreateNode($edits[$i]);
    }

    // Add a comment to the last node as other user.
    $this->drupalLogin($this->other_user);
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    $this->drupalPost('comment/reply/' . $nodes[3]->nid, $comment, t('Save'));

    // Start indexing backwards from node 3.
    variable_set('tracker_index_nid', 3);

    // Clear the current tracker tables and rebuild them.
    db_delete('tracker_node')
      ->execute();
    db_delete('tracker_user')
      ->execute();
    tracker_cron();

    $this->drupalLogin($this->user);

    // Fetch the user's tracker.
    $this->drupalGet('tracker/' . $this->user->uid);

    // Assert that all node titles are displayed.
    foreach ($nodes as $i => $node) {
      $this->assertText($node->title, format_string('Node @i is displayed on the tracker listing pages.', array('@i' => $i)));
    }
    $this->assertText('1 new', 'New comment is counted on the tracker listing pages.');
    $this->assertText('updated', 'Node is listed as updated');

    // Fetch the site-wide tracker.
    $this->drupalGet('tracker');

    // Assert that all node titles are displayed.
    foreach ($nodes as $i => $node) {
      $this->assertText($node->title, format_string('Node @i is displayed on the tracker listing pages.', array('@i' => $i)));
    }
    $this->assertText('1 new', 'New comment is counted on the tracker listing pages.');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
