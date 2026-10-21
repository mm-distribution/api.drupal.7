# _tracker_remove()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 319–388 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L319-L388)
- **Module/theme:** tracker

## Signature

```php
function _tracker_remove($nid, $uid = NULL, $changed = NULL)
```

## Documentation

```text
Cleans up indexed data when nodes or comments are removed.

@param $nid
 The node ID.
@param $uid
  The author of the node or comment.
@param $changed
  The last changed timestamp of the node.
```

## Code

```php
function _tracker_remove($nid, $uid = NULL, $changed = NULL) {
  $node = db_query('SELECT nid, status, uid, changed FROM {node} WHERE nid = :nid', array(':nid' => $nid))->fetchObject();

  // The user only keeps his or her subscription if both of the following are true:
  //   (1) The node exists.
  //   (2) The user is either the node author or has commented on the node.
  $keep_subscription = FALSE;

  if ($node) {
    // Self-authorship is one reason to keep the user's subscription.
    $keep_subscription = ($node->uid == $uid);

    // Comments are a second reason to keep the user's subscription.
    if (!$keep_subscription) {
      // Check if the user has commented at least once on the given nid.
      $keep_subscription = db_query_range('SELECT COUNT(*) FROM {comment} WHERE nid = :nid AND uid = :uid AND status = :status', 0, 1, array(
        ':nid' => $nid,
        ':uid' => $uid,
        ':status' => COMMENT_PUBLISHED,
      ))->fetchField();
    }

    // If we haven't found a reason to keep the user's subscription, delete it.
    if (!$keep_subscription) {
      db_delete('tracker_user')
        ->condition('nid', $nid)
        ->condition('uid', $uid)
        ->execute();
    }

    // Now we need to update the (possibly) changed timestamps for other users
    // and the node itself.
    // We only need to do this if the removed item has a timestamp that equals
    // or exceeds the listed changed timestamp for the node.
    $tracker_node = db_query('SELECT nid, changed FROM {tracker_node} WHERE nid = :nid', array(':nid' => $nid))->fetchObject();
    if ($tracker_node && $changed >= $tracker_node->changed) {
      // If we're here, the item being removed is *possibly* the item that
      // established the node's changed timestamp.

      // We just have to recalculate things from scratch.
      $changed = _tracker_calculate_changed($nid);

      // And then we push the out the new changed timestamp to our denormalized
      // tables.
      db_update('tracker_node')
        ->fields(array(
          'changed' => $changed,
          'published' => $node->status,
        ))
        ->condition('nid', $nid)
        ->execute();
      db_update('tracker_node')
        ->fields(array(
          'changed' => $changed,
          'published' => $node->status,
        ))
        ->condition('nid', $nid)
        ->execute();
    }
  }
  else {
    // If the node doesn't exist, remove everything.
    db_delete('tracker_node')
      ->condition('nid', $nid)
      ->execute();
    db_delete('tracker_user')
      ->condition('nid', $nid)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
