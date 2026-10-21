# search_comment_unpublish()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 850–853 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L850-L853)
- **Module/theme:** search
- **Implements:** [hook_comment_unpublish()](../../comment/comment.api.php/hook_comment_unpublish.md)

## Signature

```php
function search_comment_unpublish($comment)
```

## Documentation

```text
Implements hook_comment_unpublish().
```

## Code

```php
function search_comment_unpublish($comment) {
  // Reindex the node when comments are unpublished.
  search_touch_node($comment->nid);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
