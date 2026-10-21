# aggregator_feed_load()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 691–698 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L691-L698)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_feed_load($fid)
```

## Documentation

```text
Loads an aggregator feed.

@param $fid
  The feed id.

@return
  An object describing the feed.
```

## Code

```php
function aggregator_feed_load($fid) {
  $feeds = &drupal_static(__FUNCTION__);
  if (!isset($feeds[$fid])) {
    $feeds[$fid] = db_query('SELECT * FROM {aggregator_feed} WHERE fid = :fid', array(':fid' => $fid))->fetchObject();
  }

  return $feeds[$fid];
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
