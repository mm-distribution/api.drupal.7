# hook_cron_queue_info()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 620–626 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L620-L626)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_cron_queue_info()
```

## Documentation

```text
Declare queues holding items that need to be run periodically.

While there can be only one hook_cron() process running at the same time,
there can be any number of processes defined here running. Because of
this, long running tasks are much better suited for this API. Items queued
in hook_cron() might be processed in the same cron run if there are not many
items in the queue, otherwise it might take several requests, which can be
run in parallel.

@return
  An associative array where the key is the queue name and the value is
  again an associative array. Possible keys are:
  - 'worker callback': The name of an implementation of
    callback_queue_worker().
  - 'time': (optional) How much time Drupal should spend on calling this
    worker in seconds. Defaults to 15.
  - 'skip on cron': (optional) Set to TRUE to avoid being processed during
    cron runs (for example, if you want to control all queue execution
    manually).

@see hook_cron()
@see hook_cron_queue_info_alter()
```

## Code

```php
function hook_cron_queue_info() {
  $queues['aggregator_feeds'] = array(
    'worker callback' => 'aggregator_refresh',
    'time' => 60,
  );
  return $queues;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_cron_queue_info()".

- [aggregator_cron_queue_info()](../../aggregator/aggregator.module/aggregator_cron_queue_info.md) — `modules/aggregator/aggregator.module`
- [cron_queue_test_cron_queue_info()](../tests/cron_queue_test.module/cron_queue_test_cron_queue_info.md) — `modules/system/tests/cron_queue_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
