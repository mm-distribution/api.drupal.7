# CronQueueTestCase::testExceptions()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 990–1002 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L990-L1002)
- **Class:** [CronQueueTestCase](../CronQueueTestCase.md)
- **Module/theme:** system

## Signature

```php
function testExceptions()
```

## Documentation

```text
Tests that exceptions thrown by workers are handled properly.
```

## Code

```php
  function testExceptions() {
    $queue = DrupalQueue::get('cron_queue_test_exception');

    // Enqueue an item for processing.
    $queue->createItem(array($this->randomName() => $this->randomName()));

    // Run cron; the worker for this queue should throw an exception and handle
    // it.
    $this->cronRun();

    // The item should be left in the queue.
    $this->assertEqual($queue->numberOfItems(), 1, 'Failing item still in the queue after throwing an exception.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
