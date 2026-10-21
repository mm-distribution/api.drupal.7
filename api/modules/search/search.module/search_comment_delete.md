# search_comment_delete()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 834–837 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L834-L837)
- **Module/theme:** search
- **Implements:** [hook_comment_delete()](../../comment/comment.api.php/hook_comment_delete.md)

## Signature

```php
function search_comment_delete($comment)
```

## Documentation

```text
Implements hook_comment_delete().
```

## Code

```php
function search_comment_delete($comment) {
  // Reindex the node when comments are deleted.
  search_touch_node($comment->nid);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
