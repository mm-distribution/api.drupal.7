# forum_comment_publish()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 492–494 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L492-L494)
- **Module/theme:** forum
- **Implements:** [hook_comment_publish()](../../comment/comment.api.php/hook_comment_publish.md)

## Signature

```php
function forum_comment_publish($comment)
```

## Documentation

```text
Implements hook_comment_publish().

This actually handles the insertion and update of published nodes since
comment_save() calls hook_comment_publish() for all published comments.
```

## Code

```php
function forum_comment_publish($comment) {
  _forum_update_forum_index($comment->nid);
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
