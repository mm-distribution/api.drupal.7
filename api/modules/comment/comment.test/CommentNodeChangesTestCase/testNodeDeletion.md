# CommentNodeChangesTestCase::testNodeDeletion()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 2325–2331 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L2325-L2331)
- **Class:** [CommentNodeChangesTestCase](../CommentNodeChangesTestCase.md)
- **Module/theme:** comment

## Signature

```php
function testNodeDeletion()
```

## Documentation

```text
Tests that comments are deleted with the node.
```

## Code

```php
  function testNodeDeletion() {
    $this->drupalLogin($this->web_user);
    $comment = $this->postComment($this->node, $this->randomName(), $this->randomName());
    $this->assertTrue(comment_load($comment->id), 'The comment could be loaded.');
    node_delete($this->node->nid);
    $this->assertFalse(comment_load($comment->id), 'The comment could not be loaded after the node was deleted.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
