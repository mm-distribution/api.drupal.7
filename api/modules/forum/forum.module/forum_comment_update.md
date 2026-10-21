# forum_comment_update()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 502–508 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L502-L508)
- **Module/theme:** forum
- **Implements:** [hook_comment_update()](../../comment/comment.api.php/hook_comment_update.md)

## Signature

```php
function forum_comment_update($comment)
```

## Documentation

```text
Implements hook_comment_update().

The Comment module doesn't call hook_comment_unpublish() when saving
individual comments, so we need to check for those here.
```

## Code

```php
function forum_comment_update($comment) {
  // comment_save() calls hook_comment_publish() for all published comments,
  // so we need to handle all other values here.
  if (!$comment->status) {
    _forum_update_forum_index($comment->nid);
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
