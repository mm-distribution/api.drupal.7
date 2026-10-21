# TrackerTest::testTrackerAdminUnpublish()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 310–332 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L310-L332)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerAdminUnpublish()
```

## Documentation

```text
Tests that publish/unpublish works at admin/content/node.
```

## Code

```php
  function testTrackerAdminUnpublish() {
    $admin_user = $this->drupalCreateUser(array('access content overview', 'administer nodes', 'bypass node access'));
    $this->drupalLogin($admin_user);

    $node = $this->drupalCreateNode(array(
      'comment' => 2,
      'title' => $this->randomName(),
    ));

    // Assert that the node is displayed.
    $this->drupalGet('tracker');
    $this->assertText($node->title, 'Node is displayed on the tracker listing pages.');

    // Unpublish the node and ensure that it's no longer displayed.
    $edit = array(
      'operation' => 'unpublish',
      'nodes[' . $node->nid . ']' => $node->nid,
    );
    $this->drupalPost('admin/content', $edit, t('Update'));

    $this->drupalGet('tracker');
    $this->assertText(t('No content available.'), 'Node is displayed on the tracker listing pages.');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
