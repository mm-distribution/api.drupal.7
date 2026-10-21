# search_comment_insert()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 818–821 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L818-L821)
- **Module/theme:** search
- **Implements:** [hook_comment_insert()](../../comment/comment.api.php/hook_comment_insert.md)

## Signature

```php
function search_comment_insert($comment)
```

## Documentation

```text
Implements hook_comment_insert().
```

## Code

```php
function search_comment_insert($comment) {
  // Reindex the node when comments are added.
  search_touch_node($comment->nid);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
