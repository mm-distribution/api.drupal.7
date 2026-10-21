# system_cron_test_flush_caches()

- **Type:** Function
- **File:** [`modules/system/tests/system_cron_test.module`](_file.md), lines 11–15 · [local source](../../../../../source/modules/system/tests/system_cron_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/tests/system_cron_test.module#L11-L15)
- **Module/theme:** cron_queue_test
- **Implements:** [hook_flush_caches()](../../system.api.php/hook_flush_caches.md)

## Signature

```php
function system_cron_test_flush_caches()
```

## Documentation

```text
Implements hook_flush_caches().
```

## Code

```php
function system_cron_test_flush_caches() {
  // Set a variable to indicate that this hook was invoked.
  variable_set('system_cron_test_flush_caches', 1);
  return array();
}
```

---
_Drupal 7.103 · [modules/system/tests/system_cron_test.module](https://github.com/drupal/drupal/blob/7.103/modules/system/tests/system_cron_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
