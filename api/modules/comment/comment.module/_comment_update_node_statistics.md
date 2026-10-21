# _comment_update_node_statistics()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2460–2503 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2460-L2503)
- **Module/theme:** comment

## Signature

```php
function _comment_update_node_statistics($nid)
```

## Documentation

```text
Updates the comment statistics for a given node. This should be called any
time a comment is added, deleted, or updated.

The following fields are contained in the node_comment_statistics table.
- last_comment_timestamp: the timestamp of the last comment for this node or the node create stamp if no comments exist for the node.
- last_comment_name: the name of the anonymous poster for the last comment
- last_comment_uid: the uid of the poster for the last comment for this node or the node authors uid if no comments exists for the node.
- comment_count: the total number of approved/published comments on this node.
```

## Code

```php
function _comment_update_node_statistics($nid) {
  // Allow bulk updates and inserts to temporarily disable the
  // maintenance of the {node_comment_statistics} table.
  if (!variable_get('comment_maintain_node_statistics', TRUE)) {
    return;
  }

  $count = db_query('SELECT COUNT(cid) FROM {comment} WHERE nid = :nid AND status = :status', array(
    ':nid' => $nid,
    ':status' => COMMENT_PUBLISHED,
  ))->fetchField();

  if ($count > 0) {
    // Comments exist.
    $last_reply = db_query_range('SELECT cid, name, changed, uid FROM {comment} WHERE nid = :nid AND status = :status ORDER BY cid DESC', 0, 1, array(
      ':nid' => $nid,
      ':status' => COMMENT_PUBLISHED,
    ))->fetchObject();
    db_update('node_comment_statistics')
      ->fields(array(
        'cid' => $last_reply->cid,
        'comment_count' => $count,
        'last_comment_timestamp' => $last_reply->changed,
        'last_comment_name' => $last_reply->uid ? '' : $last_reply->name,
        'last_comment_uid' => $last_reply->uid,
      ))
      ->condition('nid', $nid)
      ->execute();
  }
  else {
    // Comments do not exist.
    $node = db_query('SELECT uid, created FROM {node} WHERE nid = :nid', array(':nid' => $nid))->fetchObject();
    db_update('node_comment_statistics')
      ->fields(array(
        'cid' => 0,
        'comment_count' => 0,
        'last_comment_timestamp' => $node->created,
        'last_comment_name' => '',
        'last_comment_uid' => $node->uid,
      ))
      ->condition('nid', $nid)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
