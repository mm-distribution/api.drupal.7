# CommentPagerTest::testCommentOrderingThreading()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1319–1389 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1319-L1389)
- **Class:** [CommentPagerTest](../CommentPagerTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentOrderingThreading()
```

## Documentation

```text
Test comment ordering and threading.
```

## Code

```php
  function testCommentOrderingThreading() {
    $this->drupalLogin($this->admin_user);

    // Set comment variables.
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentPreview(DRUPAL_DISABLED);

    // Display all the comments on the same page.
    $this->setCommentsPerPage(1000);

    // Create a node and three comments.
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $comments = array();
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);
    $comments[] = $this->postComment($node, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the second comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[1]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the first comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[0]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the last comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[2]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // Post a reply to the second comment.
    $this->drupalGet('comment/reply/' . $node->nid . '/' . $comments[3]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // At this point, the comment tree is:
    // - 0
    //   - 4
    // - 1
    //   - 3
    //     - 6
    // - 2
    //   - 5

    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_FLAT, 'Comment paging changed.');

    $expected_order = array(
      0,
      1,
      2,
      3,
      4,
      5,
      6,
    );
    $this->drupalGet('node/' . $node->nid);
    $this->assertCommentOrder($comments, $expected_order);

    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Switched to threaded mode.');

    $expected_order = array(
      0,
      4,
      1,
      3,
      6,
      2,
      5,
    );
    $this->drupalGet('node/' . $node->nid);
    $this->assertCommentOrder($comments, $expected_order);
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
