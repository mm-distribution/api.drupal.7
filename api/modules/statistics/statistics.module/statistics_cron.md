# statistics_cron()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 245–262 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L245-L262)
- **Module/theme:** statistics
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function statistics_cron()
```

## Documentation

```text
Implements hook_cron().
```

## Code

```php
function statistics_cron() {
  $statistics_timestamp = variable_get('statistics_day_timestamp', 0);

  if ((REQUEST_TIME - $statistics_timestamp) >= 86400) {
    // Reset day counts.
    db_update('node_counter')
      ->fields(array('daycount' => 0))
      ->execute();
    variable_set('statistics_day_timestamp', REQUEST_TIME);
  }

  // Clean up expired access logs (if applicable).
  if (variable_get('statistics_flush_accesslog_timer', 259200) > 0) {
    db_delete('accesslog')
      ->condition('timestamp', REQUEST_TIME - variable_get('statistics_flush_accesslog_timer', 259200), '<')
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
