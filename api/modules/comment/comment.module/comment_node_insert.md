# comment_node_insert()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1311–1326 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1311-L1326)
- **Module/theme:** comment
- **Implements:** [hook_node_insert()](../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function comment_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function comment_node_insert($node) {
  // Allow bulk updates and inserts to temporarily disable the
  // maintenance of the {node_comment_statistics} table.
  if (variable_get('comment_maintain_node_statistics', TRUE)) {
    db_insert('node_comment_statistics')
      ->fields(array(
        'nid' => $node->nid,
        'cid' => 0,
        'last_comment_timestamp' => $node->changed,
        'last_comment_name' => NULL,
        'last_comment_uid' => $node->uid,
        'comment_count' => 0,
      ))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
