# CronQueueTestCase::testCallable()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1007–1019 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1007-L1019)
- **Class:** [CronQueueTestCase](../CronQueueTestCase.md)
- **Module/theme:** system

## Signature

```php
function testCallable()
```

## Documentation

```text
Tests worker defined as a class method callable.
```

## Code

```php
  function testCallable() {
    $queue = DrupalQueue::get('cron_queue_test_callback');

    // Enqueue an item for processing.
    $queue->createItem(array($this->randomName() => $this->randomName()));

    // Run cron; the worker should perform the task and delete the item from the
    // queue.
    $this->cronRun();

    // The queue should be empty.
    $this->assertEqual($queue->numberOfItems(), 0);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
