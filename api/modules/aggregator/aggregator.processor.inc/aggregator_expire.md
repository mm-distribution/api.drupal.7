# aggregator_expire()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 193–213 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L193-L213)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_expire($feed)
```

## Documentation

```text
Expires items from a feed depending on expiration settings.

@param $feed
  Object describing feed.
```

## Code

```php
function aggregator_expire($feed) {
  $aggregator_clear = variable_get('aggregator_clear', 9676800);

  if ($aggregator_clear != AGGREGATOR_CLEAR_NEVER) {
    // Remove all items that are older than flush item timer.
    $age = REQUEST_TIME - $aggregator_clear;
    $iids = db_query('SELECT iid FROM {aggregator_item} WHERE fid = :fid AND timestamp < :timestamp', array(
      ':fid' => $feed->fid,
      ':timestamp' => $age,
    ))
    ->fetchCol();
    if ($iids) {
      db_delete('aggregator_category_item')
        ->condition('iid', $iids, 'IN')
        ->execute();
      db_delete('aggregator_item')
        ->condition('iid', $iids, 'IN')
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
