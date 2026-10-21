# _forum_update_forum_index()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 1340–1371 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L1340-L1371)
- **Module/theme:** forum

## Signature

```php
function _forum_update_forum_index($nid)
```

## Documentation

```text
Updates the taxonomy index for a given node.

@param $nid
  The ID of the node to update.
```

## Code

```php
function _forum_update_forum_index($nid) {
  $count = db_query('SELECT COUNT(cid) FROM {comment} c INNER JOIN {forum_index} i ON c.nid = i.nid WHERE c.nid = :nid AND c.status = :status', array(
    ':nid' => $nid,
    ':status' => COMMENT_PUBLISHED,
  ))->fetchField();

  if ($count > 0) {
    // Comments exist.
    $last_reply = db_query_range('SELECT cid, name, created, uid FROM {comment} WHERE nid = :nid AND status = :status ORDER BY cid DESC', 0, 1, array(
      ':nid' => $nid,
      ':status' => COMMENT_PUBLISHED,
    ))->fetchObject();
    db_update('forum_index')
      ->fields( array(
        'comment_count' => $count,
        'last_comment_timestamp' => $last_reply->created,
      ))
      ->condition('nid', $nid)
      ->execute();
  }
  else {
    // Comments do not exist.
    $node = db_query('SELECT uid, created FROM {node} WHERE nid = :nid', array(':nid' => $nid))->fetchObject();
    db_update('forum_index')
      ->fields( array(
        'comment_count' => 0,
        'last_comment_timestamp' => $node->created,
      ))
      ->condition('nid', $nid)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
