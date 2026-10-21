# search_comment_update()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 826–829 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L826-L829)
- **Module/theme:** search
- **Implements:** [hook_comment_update()](../../comment/comment.api.php/hook_comment_update.md)

## Signature

```php
function search_comment_update($comment)
```

## Documentation

```text
Implements hook_comment_update().
```

## Code

```php
function search_comment_update($comment) {
  // Reindex the node when comments are changed.
  search_touch_node($comment->nid);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
