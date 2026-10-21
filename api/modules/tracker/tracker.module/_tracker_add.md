# _tracker_add()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 250–285 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L250-L285)
- **Module/theme:** tracker

## Signature

```php
function _tracker_add($nid, $uid, $changed)
```

## Documentation

```text
Updates indexing tables when a node is added, updated, or commented on.

@param $nid
  A node ID.
@param $uid
  The node or comment author.
@param $changed
  The node updated timestamp or comment timestamp.
```

## Code

```php
function _tracker_add($nid, $uid, $changed) {
  $node = db_query('SELECT nid, status, uid, changed FROM {node} WHERE nid = :nid', array(':nid' => $nid))->fetchObject();

  // Adding a comment can only increase the changed timestamp, so our
  // calculation here is simple.
  $changed = max($node->changed, $changed);

  // Update the node-level data.
  db_merge('tracker_node')
    ->key(array('nid' => $nid))
    ->fields(array(
      'changed' => $changed,
      'published' => $node->status,
    ))
    ->execute();

  // Create or update the user-level data, first for the user posting.
  db_merge('tracker_user')
    ->key(array(
      'nid' => $nid,
      'uid' => $uid,
    ))
    ->fields(array(
      'changed' => $changed,
      'published' => $node->status,
    ))
    ->execute();
  // Update the times for all the other users tracking the post.
  db_update('tracker_user')
    ->condition('nid', $nid)
    ->fields(array(
      'changed' => $changed,
      'published' => $node->status,
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
