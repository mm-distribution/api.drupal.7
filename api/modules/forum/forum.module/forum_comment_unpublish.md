# forum_comment_unpublish()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 513–515 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L513-L515)
- **Module/theme:** forum
- **Implements:** [hook_comment_unpublish()](../../comment/comment.api.php/hook_comment_unpublish.md)

## Signature

```php
function forum_comment_unpublish($comment)
```

## Documentation

```text
Implements hook_comment_unpublish().
```

## Code

```php
function forum_comment_unpublish($comment) {
  _forum_update_forum_index($comment->nid);
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
