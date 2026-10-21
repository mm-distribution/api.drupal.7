# tracker_comment_update()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 208–214 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L208-L214)
- **Module/theme:** tracker
- **Implements:** [hook_comment_update()](../../comment/comment.api.php/hook_comment_update.md)

## Signature

```php
function tracker_comment_update($comment)
```

## Documentation

```text
Implements hook_comment_update().

Comment module doesn't call hook_comment_unpublish() when saving individual
comments so we need to check for those here.
```

## Code

```php
function tracker_comment_update($comment) {
  // comment_save() calls hook_comment_publish() for all published comments
  // so we need to handle all other values here.
  if ($comment->status != COMMENT_PUBLISHED) {
    _tracker_remove($comment->nid, $comment->uid, $comment->changed);
  }
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
