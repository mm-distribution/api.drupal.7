# TrackerTest::testTrackerOrderingNewComments()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 187–248 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L187-L248)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerOrderingNewComments()
```

## Documentation

```text
Tests for ordering on a users tracker listing when comments are posted.
```

## Code

```php
  function testTrackerOrderingNewComments() {
    $this->drupalLogin($this->user);

    $node_one = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
    ));

    $node_two = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
    ));

    // Now get other_user to track these pieces of content.
    $this->drupalLogin($this->other_user);

    // Add a comment to the first page.
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    $this->drupalPost('comment/reply/' . $node_one->nid, $comment, t('Save'));

    // If the comment is posted in the same second as the last one then Drupal
    // can't tell the difference, so we wait one second here.
    sleep(1);

    // Add a comment to the second page.
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    $this->drupalPost('comment/reply/' . $node_two->nid, $comment, t('Save'));

    // We should at this point have in our tracker for other_user:
    // 1. node_two
    // 2. node_one
    // Because that's the reverse order of the posted comments.

    // Now we're going to post a comment to node_one which should jump it to the
    // top of the list.

    $this->drupalLogin($this->user);
    // If the comment is posted in the same second as the last one then Drupal
    // can't tell the difference, so we wait one second here.
    sleep(1);

    // Add a comment to the second page.
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    $this->drupalPost('comment/reply/' . $node_one->nid, $comment, t('Save'));

    // Switch back to the other_user and assert that the order has swapped.
    $this->drupalLogin($this->other_user);
    $this->drupalGet('user/' . $this->other_user->uid . '/track');
    // This is a cheeky way of asserting that the nodes are in the right order
    // on the tracker page.
    // It's almost certainly too brittle.
    $pattern = '/' . preg_quote($node_one->title) . '.+' . preg_quote($node_two->title) . '/s';
    $this->verbose($pattern);
    $this->assertPattern($pattern, 'Most recently commented on node appears at the top of tracker');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
