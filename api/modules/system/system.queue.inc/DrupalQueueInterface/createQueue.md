# DrupalQueueInterface::createQueue()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 178–178 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L178)
- **Class:** [DrupalQueueInterface](../DrupalQueueInterface.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function createQueue();
```

## Documentation

```text
Create a queue.

Called during installation and should be used to perform any necessary
initialization operations. This should not be confused with the
constructor for these objects, which is called every time an object is
instantiated to operate on a queue. This operation is only needed the
first time a given queue is going to be initialized (for example, to make
a new database table or directory to hold tasks for the queue -- it
depends on the queue implementation if this is necessary at all).
```

## Code

```php
  public function createQueue();
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
