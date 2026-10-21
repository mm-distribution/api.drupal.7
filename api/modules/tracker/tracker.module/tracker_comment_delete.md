# tracker_comment_delete()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 236–238 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L236-L238)
- **Module/theme:** tracker
- **Implements:** [hook_comment_delete()](../../comment/comment.api.php/hook_comment_delete.md)

## Signature

```php
function tracker_comment_delete($comment)
```

## Documentation

```text
Implements hook_comment_delete().
```

## Code

```php
function tracker_comment_delete($comment) {
  _tracker_remove($comment->nid, $comment->uid, $comment->changed);
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
