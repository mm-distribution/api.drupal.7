# search_comment_publish()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 842–845 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L842-L845)
- **Module/theme:** search
- **Implements:** [hook_comment_publish()](../../comment/comment.api.php/hook_comment_publish.md)

## Signature

```php
function search_comment_publish($comment)
```

## Documentation

```text
Implements hook_comment_publish().
```

## Code

```php
function search_comment_publish($comment) {
  // Reindex the node when comments are published.
  search_touch_node($comment->nid);
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
