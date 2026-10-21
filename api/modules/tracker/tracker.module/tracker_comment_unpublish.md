# tracker_comment_unpublish()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 229–231 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L229-L231)
- **Module/theme:** tracker
- **Implements:** [hook_comment_unpublish()](../../comment/comment.api.php/hook_comment_unpublish.md)

## Signature

```php
function tracker_comment_unpublish($comment)
```

## Documentation

```text
Implements hook_comment_unpublish().
```

## Code

```php
function tracker_comment_unpublish($comment) {
  _tracker_remove($comment->nid, $comment->uid, $comment->changed);
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
