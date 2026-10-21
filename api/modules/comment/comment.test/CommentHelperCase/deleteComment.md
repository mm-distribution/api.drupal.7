# CommentHelperCase::deleteComment()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 131–134 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L131-L134)
- **Class:** [CommentHelperCase](../CommentHelperCase.md)
- **Module/theme:** comment

## Signature

```php
function deleteComment($comment)
```

## Documentation

```text
Delete comment.

@param object $comment
  Comment to delete.
```

## Code

```php
  function deleteComment($comment) {
    $this->drupalPost('comment/' . $comment->id . '/delete', array(), t('Delete'));
    $this->assertText(t('The comment and all its replies have been deleted.'), 'Comment deleted.');
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
