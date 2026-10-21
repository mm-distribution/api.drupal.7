# comment_update_index()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1382–1385 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1382-L1385)
- **Module/theme:** comment
- **Implements:** [hook_update_index()](../../search/search.api.php/hook_update_index.md)

## Signature

```php
function comment_update_index()
```

## Documentation

```text
Implements hook_update_index().
```

## Code

```php
function comment_update_index() {
  // Store the maximum possible comments per thread (used for ranking by reply count)
  variable_set('node_cron_comments_scale', 1.0 / max(1, db_query('SELECT MAX(comment_count) FROM {node_comment_statistics}')->fetchField()));
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
