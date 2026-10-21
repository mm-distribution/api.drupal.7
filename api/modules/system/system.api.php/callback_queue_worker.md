# callback_queue_worker()

- **Type:** Function
- **File:** [`modules/system/system.api.php`](_file.md), lines 4872–4876 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4872-L4876)
- **Module/theme:** system
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_queue_worker($queue_item_data)
```

## Documentation

```text
Work on a single queue item.

Callback for hook_cron_queue_info().

@param $queue_item_data
  The data that was passed to DrupalQueueInterface::createItem() when the
  item was queued.

@throws Exception
  The worker callback may throw an exception to indicate there was a problem.
  The cron process will log the exception, and leave the item in the queue to
  be processed again later.

@see drupal_cron_run()
```

## Code

```php
function callback_queue_worker($queue_item_data) {
  $node = node_load($queue_item_data);
  $node->title = 'Updated title';
  node_save($node);
}
```

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
