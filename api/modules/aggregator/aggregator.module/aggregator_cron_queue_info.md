# aggregator_cron_queue_info()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 337–343 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L337-L343)
- **Module/theme:** aggregator
- **Implements:** [hook_cron_queue_info()](../../system/system.api.php/hook_cron_queue_info.md)

## Signature

```php
function aggregator_cron_queue_info()
```

## Documentation

```text
Implements hook_cron_queue_info().
```

## Code

```php
function aggregator_cron_queue_info() {
  $queues['aggregator_feeds'] = array(
    'worker callback' => 'aggregator_refresh',
    'time' => 60,
  );
  return $queues;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
