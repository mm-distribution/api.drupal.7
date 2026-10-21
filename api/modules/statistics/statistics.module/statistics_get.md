# statistics_get()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 314–320 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L314-L320)
- **Module/theme:** statistics

## Signature

```php
function statistics_get($nid)
```

## Documentation

```text
Retrieves a node's "view statistics".

@param $nid
  The node ID.

@return
  An associative array containing:
  - totalcount: Integer for the total number of times the node has been
    viewed.
  - daycount: Integer for the total number of times the node has been viewed
    "today". For the daycount to be reset, cron must be enabled.
  - timestamp: Integer for the timestamp of when the node was last viewed.
```

## Code

```php
function statistics_get($nid) {

  if ($nid > 0) {
    // Retrieve an array with both totalcount and daycount.
    return db_query('SELECT totalcount, daycount, timestamp FROM {node_counter} WHERE nid = :nid', array(':nid' => $nid), array('target' => 'slave'))->fetchAssoc();
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
