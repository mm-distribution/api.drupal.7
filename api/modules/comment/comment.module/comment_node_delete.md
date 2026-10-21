# comment_node_delete()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1331–1337 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1331-L1337)
- **Module/theme:** comment
- **Implements:** [hook_node_delete()](../../node/node.api.php/hook_node_delete.md)

## Signature

```php
function comment_node_delete($node)
```

## Documentation

```text
Implements hook_node_delete().
```

## Code

```php
function comment_node_delete($node) {
  $cids = db_query('SELECT cid FROM {comment} WHERE nid = :nid', array(':nid' => $node->nid))->fetchCol();
  comment_delete_multiple($cids);
  db_delete('node_comment_statistics')
    ->condition('nid', $node->nid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
