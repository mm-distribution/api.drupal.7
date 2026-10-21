# comment_node_load()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1267–1297 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1267-L1297)
- **Module/theme:** comment
- **Implements:** [hook_node_load()](../../node/node.api.php/hook_node_load.md)

## Signature

```php
function comment_node_load($nodes, $types)
```

## Documentation

```text
Implements hook_node_load().
```

## Code

```php
function comment_node_load($nodes, $types) {
  $comments_enabled = array();

  // Check if comments are enabled for each node. If comments are disabled,
  // assign values without hitting the database.
  foreach ($nodes as $node) {
    // Store whether comments are enabled for this node.
    if ($node->comment != COMMENT_NODE_HIDDEN) {
      $comments_enabled[] = $node->nid;
    }
    else {
      $node->cid = 0;
      $node->last_comment_timestamp = $node->created;
      $node->last_comment_name = '';
      $node->last_comment_uid = $node->uid;
      $node->comment_count = 0;
    }
  }

  // For nodes with comments enabled, fetch information from the database.
  if (!empty($comments_enabled)) {
    $result = db_query('SELECT nid, cid, last_comment_timestamp, last_comment_name, last_comment_uid, comment_count FROM {node_comment_statistics} WHERE nid IN (:comments_enabled)', array(':comments_enabled' => $comments_enabled));
    foreach ($result as $record) {
      $nodes[$record->nid]->cid = $record->cid;
      $nodes[$record->nid]->last_comment_timestamp = $record->last_comment_timestamp;
      $nodes[$record->nid]->last_comment_name = $record->last_comment_name;
      $nodes[$record->nid]->last_comment_uid = $record->last_comment_uid;
      $nodes[$record->nid]->comment_count = $record->comment_count;
    }
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
