# comment_save_action()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2681–2685 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2681-L2685)
- **Module/theme:** comment
- **Topics:** [actions](../../../topics/actions.md)

## Signature

```php
function comment_save_action($comment)
```

## Documentation

```text
Saves a comment.

@ingroup actions
```

## Code

```php
function comment_save_action($comment) {
  comment_save($comment);
  cache_clear_all();
  watchdog('action', 'Saved comment %title', array('%title' => $comment->subject));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
