# CommentActionsTestCase::testCommentPublishUnpublishActions()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 1965–1994 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L1965-L1994)
- **Class:** [CommentActionsTestCase](../CommentActionsTestCase.md)
- **Module/theme:** comment

## Signature

```php
function testCommentPublishUnpublishActions()
```

## Documentation

```text
Test comment publish and unpublish actions.
```

## Code

```php
  function testCommentPublishUnpublishActions() {
    $this->drupalLogin($this->web_user);
    $comment_text = $this->randomName();
    $subject = $this->randomName();
    $comment = $this->postComment($this->node, $comment_text, $subject);
    $comment = comment_load($comment->id);

    // Unpublish a comment (direct form: doesn't actually save the comment).
    comment_unpublish_action($comment);
    $this->assertEqual($comment->status, COMMENT_NOT_PUBLISHED, 'Comment was unpublished');
    $this->assertWatchdogMessage('Unpublished comment %subject.', array('%subject' => $subject), 'Found watchdog message');
    $this->clearWatchdog();

    // Unpublish a comment (indirect form: modify the comment in the database).
    comment_unpublish_action(NULL, array('cid' => $comment->cid));
    $this->assertEqual(comment_load($comment->cid)->status, COMMENT_NOT_PUBLISHED, 'Comment was unpublished');
    $this->assertWatchdogMessage('Unpublished comment %subject.', array('%subject' => $subject), 'Found watchdog message');

    // Publish a comment (direct form: doesn't actually save the comment).
    comment_publish_action($comment);
    $this->assertEqual($comment->status, COMMENT_PUBLISHED, 'Comment was published');
    $this->assertWatchdogMessage('Published comment %subject.', array('%subject' => $subject), 'Found watchdog message');
    $this->clearWatchdog();

    // Publish a comment (indirect form: modify the comment in the database).
    comment_publish_action(NULL, array('cid' => $comment->cid));
    $this->assertEqual(comment_load($comment->cid)->status, COMMENT_PUBLISHED, 'Comment was published');
    $this->assertWatchdogMessage('Published comment %subject.', array('%subject' => $subject), 'Found watchdog message');
    $this->clearWatchdog();
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
