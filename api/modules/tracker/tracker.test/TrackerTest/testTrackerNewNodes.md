# TrackerTest::testTrackerNewNodes()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 121–144 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L121-L144)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerNewNodes()
```

## Documentation

```text
Tests for the presence of the "new" flag for nodes.
```

## Code

```php
  function testTrackerNewNodes() {
    $this->drupalLogin($this->user);

    $edit = array(
      'title' => $this->randomName(8),
    );

    $node = $this->drupalCreateNode($edit);
    $title = $edit['title'];
    $this->drupalGet('tracker');
    $this->assertPattern('/' . $title . '.*new/', 'New nodes are flagged as such in the tracker listing.');

    $this->drupalGet('node/' . $node->nid);
    $this->drupalGet('tracker');
    $this->assertNoPattern('/' . $title . '.*new/', 'Visited nodes are not flagged as new.');

    $this->drupalLogin($this->other_user);
    $this->drupalGet('tracker');
    $this->assertPattern('/' . $title . '.*new/', 'For another user, new nodes are flagged as such in the tracker listing.');

    $this->drupalGet('node/' . $node->nid);
    $this->drupalGet('tracker');
    $this->assertNoPattern('/' . $title . '.*new/', 'For another user, visited nodes are not flagged as new.');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
