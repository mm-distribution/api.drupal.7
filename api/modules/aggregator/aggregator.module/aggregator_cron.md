# aggregator_cron()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 311–332 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L311-L332)
- **Module/theme:** aggregator
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function aggregator_cron()
```

## Documentation

```text
Implements hook_cron().

Queues news feeds for updates once their refresh interval has elapsed.
```

## Code

```php
function aggregator_cron() {
  $result = db_query('SELECT * FROM {aggregator_feed} WHERE queued = 0 AND checked + refresh < :time AND refresh <> :never', array(
    ':time' => REQUEST_TIME,
    ':never' => AGGREGATOR_CLEAR_NEVER
  ));
  $queue = DrupalQueue::get('aggregator_feeds');
  foreach ($result as $feed) {
    if ($queue->createItem($feed)) {
      // Add timestamp to avoid queueing item more than once.
      db_update('aggregator_feed')
        ->fields(array('queued' => REQUEST_TIME))
        ->condition('fid', $feed->fid)
        ->execute();
    }
  }

  // Remove queued timestamp after 6 hours assuming the update has failed.
  db_update('aggregator_feed')
    ->fields(array('queued' => 0))
    ->condition('queued', REQUEST_TIME - (3600 * 6), '<')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
