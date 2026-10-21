# drupal_cron_cleanup()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5642–5650 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5642-L5650)

## Signature

```php
function drupal_cron_cleanup()
```

## Documentation

```text
DEPRECATED: Shutdown function: Performs cron cleanup.

This function is deprecated because the 'cron_semaphore' variable it
references no longer exists. It is therefore no longer used as a shutdown
function by Drupal core.

@deprecated
```

## Code

```php
function drupal_cron_cleanup() {
  // See if the semaphore is still locked.
  if (variable_get('cron_semaphore', FALSE)) {
    watchdog('cron', 'Cron run exceeded the time limit and was aborted.', array(), WATCHDOG_WARNING);

    // Release cron semaphore.
    variable_del('cron_semaphore');
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
