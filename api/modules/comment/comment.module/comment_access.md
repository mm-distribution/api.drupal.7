# comment_access()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1451–1457 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1451-L1457)
- **Module/theme:** comment

## Signature

```php
function comment_access($op, $comment)
```

## Documentation

```text
Determines whether the current user has access to a particular comment.

Authenticated users can edit their comments as long they have not been
replied to. This prevents people from changing or revising their statements
based on the replies to their posts.

@param $op
  The operation that is to be performed on the comment. Only 'edit' is
  recognized now.
@param $comment
  The comment object.
@return
  TRUE if the current user has acces to the comment, FALSE otherwise.
```

## Code

```php
function comment_access($op, $comment) {
  global $user;

  if ($op == 'edit') {
    return ($user->uid && $user->uid == $comment->uid && $comment->status == COMMENT_PUBLISHED && user_access('edit own comments')) || user_access('administer comments');
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
