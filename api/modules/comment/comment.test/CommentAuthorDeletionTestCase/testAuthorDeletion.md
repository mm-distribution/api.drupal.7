# CommentAuthorDeletionTestCase::testAuthorDeletion()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2349–2363 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2349-L2363)
- **Class:** [CommentAuthorDeletionTestCase](../CommentAuthorDeletionTestCase.md)
- **Module/theme:** comment

## Signature

```php
function testAuthorDeletion()
```

## Documentation

```text
Tests that comments are correctly deleted when their author is deleted.
```

## Code

```php
  function testAuthorDeletion() {
    // Create a comment as the admin user.
    $this->drupalLogin($this->admin_user);
    $comment = $this->postComment($this->node, $this->randomName());
    $this->assertTrue($this->commentExists($comment), t('Comment is displayed initially.'));
    $this->drupalLogout();

    // Delete the admin user, and check that the node which displays the
    // comment can still be viewed, but the comment itself does not appear
    // there.
    user_delete($this->admin_user->uid);
    $this->drupalGet('node/' . $this->node->nid);
    $this->assertResponse(200, t('Node page is accessible after the comment author is deleted.'));
    $this->assertFalse($this->commentExists($comment), t('Comment is not displayed after the comment author is deleted.'));
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
