# MemoryQueue

- **Type:** Class
- **File:** [`modules/system/system.queue.inc`](_file.md), lines 296–367 · [local source](../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L296-L367)
- **Module/theme:** system
- **Topics:** [queue](../../../topics/queue.md)

## Signature

```php
class MemoryQueue implements DrupalQueueInterface
```

## Documentation

```text
Static queue implementation.

This allows "undelayed" variants of processes relying on the Queue
interface. The queue data resides in memory. It should only be used for
items that will be queued and dequeued within a given page request.
```

## Properties

### $queue

```php
protected $queue;
```

```text
The queue data.

@var array
```

### $id_sequence

```php
protected $id_sequence;
```

```text
Counter for item ids.

@var int
```

## Methods (derived index)

- [__construct()](MemoryQueue/__construct.md) — Start working with a queue.
- [createItem()](MemoryQueue/createItem.md)
- [numberOfItems()](MemoryQueue/numberOfItems.md)
- [claimItem()](MemoryQueue/claimItem.md)
- [deleteItem()](MemoryQueue/deleteItem.md)
- [releaseItem()](MemoryQueue/releaseItem.md)
- [createQueue()](MemoryQueue/createQueue.md)
- [deleteQueue()](MemoryQueue/deleteQueue.md)

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
