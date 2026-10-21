# _tracker_calculate_changed()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 297–307 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L297-L307)
- **Module/theme:** tracker

## Signature

```php
function _tracker_calculate_changed($nid)
```

## Documentation

```text
Determines the max timestamp between $node->changed and the last comment.

@param $nid
  A node ID.

@return
 The $node->changed timestamp, or most recent comment timestamp, whichever
 is the greatest.
```

## Code

```php
function _tracker_calculate_changed($nid) {
  $changed = db_query('SELECT changed FROM {node} WHERE nid = :nid', array(':nid' => $nid), array('target' => 'slave'))->fetchField();
  $latest_comment = db_query_range('SELECT cid, changed FROM {comment} WHERE nid = :nid AND status = :status ORDER BY changed DESC', 0, 1, array(
    ':nid' => $nid,
    ':status' => COMMENT_PUBLISHED,
  ), array('target' => 'slave'))->fetchObject();
  if ($latest_comment && $latest_comment->changed > $changed) {
    $changed = $latest_comment->changed;
  }
  return $changed;
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
