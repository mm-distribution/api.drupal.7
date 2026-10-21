# system_run_automated_cron()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3578–3588 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3578-L3588)
- **Module/theme:** system

## Signature

```php
function system_run_automated_cron()
```

## Documentation

```text
Run the automated cron if enabled.
```

## Code

```php
function system_run_automated_cron() {
  // If the site is not fully installed, suppress the automated cron run.
  // Otherwise it could be triggered prematurely by Ajax requests during
  // installation.
  if (($threshold = variable_get('cron_safe_threshold', DRUPAL_CRON_DEFAULT_THRESHOLD)) > 0 && variable_get('install_task') == 'done') {
    $cron_last = variable_get('cron_last', NULL);
    if (!isset($cron_last) || (REQUEST_TIME - $cron_last > $threshold)) {
      drupal_cron_run();
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
