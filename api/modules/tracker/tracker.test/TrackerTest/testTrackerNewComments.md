# TrackerTest::testTrackerNewComments()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 149–182 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L149-L182)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerNewComments()
```

## Documentation

```text
Tests for comment counters on the tracker listing.
```

## Code

```php
  function testTrackerNewComments() {
    $this->drupalLogin($this->user);

    $node = $this->drupalCreateNode(array(
      'comment' => 2,
    ));

    // Add a comment to the page.
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    // The new comment is automatically viewed by the current user.
    $this->drupalPost('comment/reply/' . $node->nid, $comment, t('Save'));

    $this->drupalLogin($this->other_user);
    $this->drupalGet('tracker');
    $this->assertText('1 new', 'New comments are counted on the tracker listing pages.');
    $this->drupalGet('node/' . $node->nid);

    // Add another comment as other_user.
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    // If the comment is posted in the same second as the last one then Drupal
    // can't tell the difference, so we wait one second here.
    sleep(1);
    $this->drupalPost('comment/reply/' . $node->nid, $comment, t('Save'));

    $this->drupalLogin($this->user);
    $this->drupalGet('tracker');
    $this->assertText('1 new', 'New comments are counted on the tracker listing pages.');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
