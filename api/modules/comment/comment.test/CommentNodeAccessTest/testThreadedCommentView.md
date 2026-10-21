# CommentNodeAccessTest::testThreadedCommentView()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1525–1562 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1525-L1562)
- **Class:** [CommentNodeAccessTest](../CommentNodeAccessTest.md)
- **Module/theme:** comment

## Signature

```php
function testThreadedCommentView()
```

## Documentation

```text
Test that threaded comments can be viewed.
```

## Code

```php
  function testThreadedCommentView() {
    $langcode = LANGUAGE_NONE;
    // Set comments to have subject required and preview disabled.
    $this->drupalLogin($this->admin_user);
    $this->setCommentPreview(DRUPAL_DISABLED);
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Comment paging changed.');
    $this->drupalLogout();

    // Post comment.
    $this->drupalLogin($this->web_user);
    $comment_text = $this->randomName();
    $comment_subject = $this->randomName();
    $comment = $this->postComment($this->node, $comment_text, $comment_subject);
    $comment_loaded = comment_load($comment->id);
    $this->assertTrue($this->commentExists($comment), 'Comment found.');

    // Check comment display.
    $this->drupalGet('node/' . $this->node->nid . '/' . $comment->id);
    $this->assertText($comment_subject, 'Individual comment subject found.');
    $this->assertText($comment_text, 'Individual comment body found.');

    // Reply to comment, creating second comment.
    $this->drupalGet('comment/reply/' . $this->node->nid . '/' . $comment->id);
    $reply_text = $this->randomName();
    $reply_subject = $this->randomName();
    $reply = $this->postComment(NULL, $reply_text, $reply_subject, TRUE);
    $reply_loaded = comment_load($reply->id);
    $this->assertTrue($this->commentExists($reply, TRUE), 'Reply found.');

    // Go to the node page and verify comment and reply are visible.
    $this->drupalGet('node/' . $this->node->nid);
    $this->assertText($comment_text);
    $this->assertText($comment_subject);
    $this->assertText($reply_text);
    $this->assertText($reply_subject);
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
