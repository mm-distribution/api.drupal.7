# announcements_feed_cron()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.module`](_file.md), lines 164–179 · [local source](../../../../source/modules/announcements_feed/announcements_feed.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module#L164-L179)
- **Module/theme:** announcements_feed
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function announcements_feed_cron()
```

## Documentation

```text
Implements hook_cron().
```

## Code

```php
function announcements_feed_cron() {
  module_load_include('inc', 'announcements_feed', 'announcements_feed');
  $cron_interval = variable_get('announcements_feed_cron_interval', ANNOUNCEMENTS_FEED_DEFAULT_CRON_INTERVAL);
  $last_check = variable_get('announcements_feed_last_fetch', 0);
  $time = time();
  if (($time - $last_check) > $cron_interval) {
    try {
      announcements_feed_fetch(TRUE);
      // Update the last_fetch variable to the current time.
      variable_set('announcements_feed_last_fetch', $time);
    }
    catch (Exception $e) {
      watchdog('announcements_feed', 'Exception occurred: @message', array('@message' => $e->getMessage()), WATCHDOG_ERROR);
    }
  }
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.module](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.module) · Licensed GPL-2.0-or-later (see LICENSE)._
