# cron_queue_test_cron_queue_info()

- **Type:** Function
- **File:** [`modules/system/tests/cron_queue_test.module`](_file.md), lines 6–15 · [local source](../../../../../source/modules/system/tests/cron_queue_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/tests/cron_queue_test.module#L6-L15)
- **Module/theme:** cron_queue_test
- **Implements:** [hook_cron_queue_info()](../../system.api.php/hook_cron_queue_info.md)

## Signature

```php
function cron_queue_test_cron_queue_info()
```

## Documentation

```text
Implements hook_cron_queue_info().
```

## Code

```php
function cron_queue_test_cron_queue_info() {
  $queues['cron_queue_test_exception'] = array(
    'worker callback' => 'cron_queue_test_exception',
  );
  $queues['cron_queue_test_callback'] = array(
    'worker callback' => array('CronQueueTestCallbackClass', 'foo'),
  );

  return $queues;
}
```

---
_Drupal 7.103 · [modules/system/tests/cron_queue_test.module](https://github.com/drupal/drupal/blob/7.103/modules/system/tests/cron_queue_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
