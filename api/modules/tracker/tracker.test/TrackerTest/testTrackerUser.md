# TrackerTest::testTrackerUser()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 75–116 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L75-L116)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function testTrackerUser()
```

## Documentation

```text
Tests for the presence of nodes on a user's tracker listing.
```

## Code

```php
  function testTrackerUser() {
    $this->drupalLogin($this->user);

    $unpublished = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
      'uid' => $this->user->uid,
      'status' => 0,
    ));
    $my_published = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
      'uid' => $this->user->uid,
      'status' => 1,
    ));
    $other_published_no_comment = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
      'uid' => $this->other_user->uid,
      'status' => 1,
    ));
    $other_published_my_comment = $this->drupalCreateNode(array(
      'title' => $this->randomName(8),
      'uid' => $this->other_user->uid,
      'status' => 1,
    ));
    $comment = array(
      'subject' => $this->randomName(),
      'comment_body[' . LANGUAGE_NONE . '][0][value]' => $this->randomName(20),
    );
    $this->drupalPost('comment/reply/' . $other_published_my_comment->nid, $comment, t('Save'));

    $this->drupalGet('user/' . $this->user->uid . '/track');
    $this->assertNoText($unpublished->title, "Unpublished nodes do not show up in the users's tracker listing.");
    $this->assertText($my_published->title, "Published nodes show up in the user's tracker listing.");
    $this->assertNoText($other_published_no_comment->title, "Other user's nodes do not show up in the user's tracker listing.");
    $this->assertText($other_published_my_comment->title, "Nodes that the user has commented on appear in the user's tracker listing.");

    // Verify that unpublished comments are removed from the tracker.
    $admin_user = $this->drupalCreateUser(array('administer comments', 'access user profiles'));
    $this->drupalLogin($admin_user);
    $this->drupalPost('comment/1/edit', array('status' => COMMENT_NOT_PUBLISHED), t('Save'));
    $this->drupalGet('user/' . $this->user->uid . '/track');
    $this->assertNoText($other_published_my_comment->title, 'Unpublished comments are not counted on the tracker listing.');
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
