# tracker_comment_publish()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 222–224 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L222-L224)
- **Module/theme:** tracker
- **Implements:** [hook_comment_publish()](../../comment/comment.api.php/hook_comment_publish.md)

## Signature

```php
function tracker_comment_publish($comment)
```

## Documentation

```text
Implements hook_comment_publish().

This actually handles the insert and update of published nodes since
comment_save() calls hook_comment_publish() for all published comments.
```

## Code

```php
function tracker_comment_publish($comment) {
  _tracker_add($comment->nid, $comment->uid, $comment->changed);
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
