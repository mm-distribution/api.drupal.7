# CommentController::attachLoad()

- **Type:** Method
- **File:** [`modules/comment/comment.module`](../_file.md), lines 1722–1731 · [local source](../../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1722-L1731)
- **Class:** [CommentController](../CommentController.md)
- **Module/theme:** comment

## Signature

```php
protected function attachLoad(&$comments, $revision_id = FALSE)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function attachLoad(&$comments, $revision_id = FALSE) {
    // Setup standard comment properties.
    foreach ($comments as $key => $comment) {
      $comment->name = $comment->uid ? $comment->registered_name : $comment->name;
      $comment->new = node_mark($comment->nid, $comment->changed);
      $comment->node_type = 'comment_node_' . $comment->node_type;
      $comments[$key] = $comment;
    }
    parent::attachLoad($comments, $revision_id);
  }
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
