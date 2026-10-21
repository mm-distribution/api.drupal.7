# CommentAuthorDeletionTestCase::testAuthorDeletionCommentModuleDisabled()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2368–2385 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2368-L2385)
- **Class:** [CommentAuthorDeletionTestCase](../CommentAuthorDeletionTestCase.md)
- **Module/theme:** comment

## Signature

```php
function testAuthorDeletionCommentModuleDisabled()
```

## Documentation

```text
Test comment author deletion while the comment module is disabled.
```

## Code

```php
  function testAuthorDeletionCommentModuleDisabled() {
    // Create a comment as the admin user.
    $this->drupalLogin($this->admin_user);
    $comment = $this->postComment($this->node, $this->randomName());
    $this->assertTrue($this->commentExists($comment), t('Comment is displayed initially.'));
    $this->drupalLogout();

    // Delete the admin user while the comment module is disabled, and ensure
    // that the missing comment author is still handled correctly (the node
    // itself should be displayed, but the comment should not be displayed on
    // it).
    module_disable(array('comment'));
    user_delete($this->admin_user->uid);
    module_enable(array('comment'));
    $this->drupalGet('node/' . $this->node->nid);
    $this->assertResponse(200, t('Node page is accessible after the comment author is deleted.'));
    $this->assertFalse($this->commentExists($comment), t('Comment is not displayed after the comment author is deleted.'));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
