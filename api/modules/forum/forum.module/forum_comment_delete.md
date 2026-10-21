# forum_comment_delete()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 520–522 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L520-L522)
- **Module/theme:** forum
- **Implements:** [hook_comment_delete()](../../comment/comment.api.php/hook_comment_delete.md)

## Signature

```php
function forum_comment_delete($comment)
```

## Documentation

```text
Implements hook_comment_delete().
```

## Code

```php
function forum_comment_delete($comment) {
  _forum_update_forum_index($comment->nid);
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
