# CommentActionsTestCase::testCommentPublishUnpublishHooks()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2034–2060 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2034-L2060)
- **Class:** [CommentActionsTestCase](../CommentActionsTestCase.md)
- **Module/theme:** comment

## Signature

```php
function testCommentPublishUnpublishHooks()
```

## Documentation

```text
Test comment publish and unpublish hooks.
```

## Code

```php
  function testCommentPublishUnpublishHooks() {
    $this->drupalLogin($this->web_user);
    module_enable(array('comment_hook_test'));
    $_SESSION['comment_hook_test'] = array();

    // Publishing a comment should trigger hook_comment_publish().
    $comment = (object) array(
      'cid' => NULL,
      'nid' => $this->node->nid,
      'node_type' => $this->node->type,
      'pid' => 0,
      'uid' => $this->loggedInUser->uid,
      'status' => COMMENT_PUBLISHED,
      'subject' => $this->randomName(),
      'hostname' => ip_address(),
      'language' => LANGUAGE_NONE,
      'comment_body' => array(LANGUAGE_NONE => array($this->randomName())),
    );
    comment_save($comment);
    $this->assertHookMessage('comment_hook_test_comment_publish called');

    // Unpublishing a comment should trigger hook_comment_unpublish().
    $comment = comment_load($comment->cid);
    $comment->status = COMMENT_NOT_PUBLISHED;
    comment_save($comment);
    $this->assertHookMessage('comment_hook_test_comment_unpublish called');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
