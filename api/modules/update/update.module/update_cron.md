# update_cron()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 297–321 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L297-L321)
- **Module/theme:** update
- **Implements:** [hook_cron()](../../system/system.api.php/hook_cron.md)

## Signature

```php
function update_cron()
```

## Documentation

```text
Implements hook_cron().
```

## Code

```php
function update_cron() {
  $frequency = variable_get('update_check_frequency', 1);
  $interval = 60 * 60 * 24 * $frequency;
  if ((REQUEST_TIME - variable_get('update_last_check', 0)) > $interval) {
    // If the configured update interval has elapsed, we want to invalidate
    // the cached data for all projects, attempt to re-fetch, and trigger any
    // configured notifications about the new status.
    update_refresh();
    update_fetch_data();
  }
  else {
    // Otherwise, see if any individual projects are now stale or still
    // missing data, and if so, try to fetch the data.
    update_get_available(TRUE);
  }
  if ((REQUEST_TIME - variable_get('update_last_email_notification', 0)) > $interval) {
    // If configured time between notifications elapsed, send email about
    // updates possibly available.
    module_load_include('inc', 'update', 'update.fetch');
    _update_cron_notify();
  }

  // Clear garbage from disk.
  update_clear_update_disk_cache();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
