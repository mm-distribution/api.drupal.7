# tracker_cron()

- **Type:** Function
- **File:** [`modules/tracker/tracker.module`](_file.md), lines 79–153 · [local source](../../../../source/modules/tracker/tracker.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module#L79-L153)
- **Module/theme:** tracker
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function tracker_cron()
```

## Documentation

```text
Implements hook_cron().

Updates tracking information for any items still to be tracked. The variable
'tracker_index_nid' is set to ((the last node ID that was indexed) - 1) and
used to select the nodes to be processed. If there are no remaining nodes to
process, 'tracker_index_nid' will be 0.
```

## Code

```php
function tracker_cron() {
  $max_nid = variable_get('tracker_index_nid', 0);
  $batch_size = variable_get('tracker_batch_size', 1000);
  if ($max_nid > 0) {
    $last_nid = FALSE;
    $result = db_query_range('SELECT nid, uid, status FROM {node} WHERE nid <= :max_nid ORDER BY nid DESC', 0, $batch_size, array(':max_nid' => $max_nid), array('target' => 'slave'));

    $count = 0;

    foreach ($result as $row) {
      // Calculate the changed timestamp for this node.
      $changed = _tracker_calculate_changed($row->nid);

      // Remove existing data for this node.
      db_delete('tracker_node')
        ->condition('nid', $row->nid)
        ->execute();
      db_delete('tracker_user')
        ->condition('nid', $row->nid)
        ->execute();

      // Insert the node-level data.
      db_insert('tracker_node')
        ->fields(array(
          'nid' => $row->nid,
          'published' => $row->status,
          'changed' => $changed,
        ))
        ->execute();

      // Insert the user-level data for the node's author.
      db_insert('tracker_user')
        ->fields(array(
          'nid' => $row->nid,
          'published' => $row->status,
          'changed' => $changed,
          'uid' => $row->uid,
        ))
        ->execute();

      $query = db_select('comment', 'c', array('target' => 'slave'));
      // Force PostgreSQL to do an implicit cast by adding 0.
      $query->addExpression('0 + :changed', 'changed', array(':changed' => $changed));
      $query->addField('c', 'status', 'published');
      $query
        ->distinct()
        ->fields('c', array('uid', 'nid'))
        ->condition('c.nid', $row->nid)
        ->condition('c.uid', $row->uid, '<>')
        ->condition('c.status', COMMENT_PUBLISHED);

      // Insert the user-level data for the commenters (except if a commenter
      // is the node's author).
      db_insert('tracker_user')
        ->from($query)
        ->execute();

      // Note that we have indexed at least one node.
      $last_nid = $row->nid;

      $count++;
    }

    if ($last_nid !== FALSE) {
      // Prepare a starting point for the next run.
      variable_set('tracker_index_nid', $last_nid - 1);

      watchdog('tracker', 'Indexed %count content items for tracking.', array('%count' => $count));
    }
    else {
      // If all nodes have been indexed, set to zero to skip future cron runs.
      variable_set('tracker_index_nid', 0);
    }
  }
}
```

---
_Drupal 7.103 · [modules/tracker/tracker.module](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.module) · Licensed GPL-2.0-or-later (see LICENSE)._
