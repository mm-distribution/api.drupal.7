# TrackerTest::testTrackerAll()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 49–70 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L49-L70)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerAll()
```

## Documentation

```text
Tests for the presence of nodes on the global tracker listing.
```

## Code

```php
  function testTrackerAll() {
    $this->drupalLogin($this->user);

    $unpublished = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
      'status' => 0,
    ));
    $published = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
      'status' => 1,
    ));

    $this->drupalGet('tracker');
    $this->assertNoText($unpublished->title, 'Unpublished node do not show up in the tracker listing.');
    $this->assertText($published->title, 'Published node show up in the tracker listing.');
    $this->assertLink(t('My recent content'), 0, 'User tab shows up on the global tracker page.');

    // Delete a node and ensure it no longer appears on the tracker.
    node_delete($published->nid);
    $this->drupalGet('tracker');
    $this->assertNoText($published->title, 'Deleted node do not show up in the tracker listing.');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
