# hook_node_update_index()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 738–745 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L738-L745)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_update_index($node)
```

## Documentation

```text
Act on a node being indexed for searching.

This hook is invoked during search indexing, after node_load(), and after the
result of node_view() is added as $node->rendered to the node object.

@param $node
  The node being indexed.

@return string
  Additional node information to be indexed.

@ingroup node_api_hooks
```

## Code

```php
function hook_node_update_index($node) {
  $text = '';
  $comments = db_query('SELECT subject, comment, format FROM {comment} WHERE nid = :nid AND status = :status', array(':nid' => $node->nid, ':status' => COMMENT_PUBLISHED));
  foreach ($comments as $comment) {
    $text .= '<h2>' . check_plain($comment->subject) . '</h2>' . check_markup($comment->comment, $comment->format, '', TRUE);
  }
  return $text;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_update_index()".

- [comment_node_update_index()](../../comment/comment.module/comment_node_update_index.md) — `modules/comment/comment.module`
- [search_node_update_index()](../../search/search.module/search_node_update_index.md) — `modules/search/search.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
