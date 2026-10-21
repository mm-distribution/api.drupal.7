# comment_node_search_result()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1393–1403 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1393-L1403)
- **Module/theme:** comment
- **Implements:** [hook_node_search_result()](../../node/node.api.php/hook_node_search_result.md)

## Signature

```php
function comment_node_search_result($node)
```

## Documentation

```text
Implements hook_node_search_result().

Formats a comment count string and returns it, for display with search
results.
```

## Code

```php
function comment_node_search_result($node) {
  // Do not make a string if comments are hidden.
  if (user_access('access comments') && $node->comment != COMMENT_NODE_HIDDEN) {
    $comments = db_query('SELECT comment_count FROM {node_comment_statistics} WHERE nid = :nid', array('nid' => $node->nid))->fetchField();
    // Do not make a string if comments are closed and there are currently
    // zero comments.
    if ($node->comment != COMMENT_NODE_CLOSED || $comments > 0) {
      return array('comment' => format_plural($comments, '1 comment', '@count comments'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
