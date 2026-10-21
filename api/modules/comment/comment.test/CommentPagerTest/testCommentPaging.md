# CommentPagerTest::testCommentPaging()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1246–1314 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1246-L1314)
- **Class:** [CommentPagerTest](../CommentPagerTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentPaging()
```

## Documentation

```text
Confirm comment paging works correctly with flat and threaded comments.
```

## Code

```php
  function testCommentPaging() {
    $this->drupalLogin($this->admin_user);

    // Set comment variables.
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentPreview(DRUPAL_DISABLED);

    // Create a node and three comments.
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $comments = array();
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);

    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_FLAT, 'Comment paging changed.');

    // Set comments to one per page so that we are able to test paging without
    // needing to insert large numbers of comments.
    $this->setCommentsPerPage(1);

    // Check the first page of the node, and confirm the correct comments are
    // shown.
    $this->drupalGet('node/' . $node->nid);
    $this->assertRaw(t('next'), 'Paging links found.');
    $this->assertTrue($this->commentExists($comments[0]), 'Comment 1 appears on page 1.');
    $this->assertFalse($this->commentExists($comments[1]), 'Comment 2 does not appear on page 1.');
    $this->assertFalse($this->commentExists($comments[2]), 'Comment 3 does not appear on page 1.');

    // Check the second page.
    $this->drupalGet('node/' . $node->nid, array('query' => array('page' => 1)));
    $this->assertTrue($this->commentExists($comments[1]), 'Comment 2 appears on page 2.');
    $this->assertFalse($this->commentExists($comments[0]), 'Comment 1 does not appear on page 2.');
    $this->assertFalse($this->commentExists($comments[2]), 'Comment 3 does not appear on page 2.');

    // Check the third page.
    $this->drupalGet('node/' . $node->nid, array('query' => array('page' => 2)));
    $this->assertTrue($this->commentExists($comments[2]), 'Comment 3 appears on page 3.');
    $this->assertFalse($this->commentExists($comments[0]), 'Comment 1 does not appear on page 3.');
    $this->assertFalse($this->commentExists($comments[1]), 'Comment 2 does not appear on page 3.');

    // Post a reply to the oldest comment and test again.
    $replies = array();
    $oldest_comment = reset($comments);
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $oldest_comment->id);
    $reply = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    $this->setCommentsPerPage(2);
    // We are still in flat view - the replies should not be on the first page,
    // even though they are replies to the oldest comment.
    $this->drupalGet('node/' . $node->nid, array('query' => array('page' => 0)));
    $this->assertFalse($this->commentExists($reply, TRUE), 'In flat mode, reply does not appear on page 1.');

    // If we switch to threaded mode, the replies on the oldest comment
    // should be bumped to the first page and comment 6 should be bumped
    // to the second page.
    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Switched to threaded mode.');
    $this->drupalGet('node/' . $node->nid, array('query' => array('page' => 0)));
    $this->assertTrue($this->commentExists($reply, TRUE), 'In threaded mode, reply appears on page 1.');
    $this->assertFalse($this->commentExists($comments[1]), 'In threaded mode, comment 2 has been bumped off of page 1.');

    // If (# replies > # comments per page) in threaded expanded view,
    // the overage should be bumped.
    $reply2 = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);
    $this->drupalGet('node/' . $node->nid, array('query' => array('page' => 0)));
    $this->assertFalse($this->commentExists($reply2, TRUE), 'In threaded mode where # replies > # comments per page, the newest reply does not appear on page 1.');

    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
