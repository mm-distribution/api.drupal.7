# Queue operations

- **Topic id:** `queue`
- **Defined in:** [`modules/system/system.queue.inc`](../modules/system/system.queue.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L8)

## Documentation

```text
@defgroup queue Queue operations
@{
Queue items to allow later processing.

The queue system allows placing items in a queue and processing them later.
The system tries to ensure that only one consumer can process an item.

Before a queue can be used it needs to be created by
DrupalQueueInterface::createQueue().

Items can be added to the queue by passing an arbitrary data object to
DrupalQueueInterface::createItem().

To process an item, call DrupalQueueInterface::claimItem() and specify how
long you want to have a lease for working on that item. When finished
processing, the item needs to be deleted by calling
DrupalQueueInterface::deleteItem(). If the consumer dies, the item will be
made available again by the DrupalQueueInterface implementation once the
lease expires. Another consumer will then be able to receive it when calling
DrupalQueueInterface::claimItem(). Due to this, the processing code should
be aware that an item might be handed over for processing more than once.

The $item object used by the DrupalQueueInterface can contain arbitrary
metadata depending on the implementation. Systems using the interface should
only rely on the data property which will contain the information passed to
DrupalQueueInterface::createItem(). The full queue item returned by
DrupalQueueInterface::claimItem() needs to be passed to
DrupalQueueInterface::deleteItem() once processing is completed.

There are two kinds of queue backends available: reliable, which preserves
the order of messages and guarantees that every item will be executed at
least once. The non-reliable kind only does a best effort to preserve order
in messages and to execute them at least once but there is a small chance
that some items get lost. For example, some distributed back-ends like
Amazon SQS will be managing jobs for a large set of producers and consumers
where a strict FIFO ordering will likely not be preserved. Another example
would be an in-memory queue backend which might lose items if it crashes.
However, such a backend would be able to deal with significantly more writes
than a reliable queue and for many tasks this is more important. See
aggregator_cron() for an example of how to effectively utilize a
non-reliable queue. Another example is doing Twitter statistics -- the small
possibility of losing a few items is insignificant next to power of the
queue being able to keep up with writes. As described in the processing
section, regardless of the queue being reliable or not, the processing code
should be aware that an item might be handed over for processing more than
once (because the processing code might time out before it finishes).
```

## Members (derived, 29)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [DrupalQueue](../modules/system/system.queue.inc/DrupalQueue.md) (class) — Factory class for interacting with queues.
- [DrupalQueueInterface](../modules/system/system.queue.inc/DrupalQueueInterface.md) (interface)
- [DrupalReliableQueueInterface](../modules/system/system.queue.inc/DrupalReliableQueueInterface.md) (interface) — Reliable queue interface.
- [MemoryQueue](../modules/system/system.queue.inc/MemoryQueue.md) (class) — Static queue implementation.
- [SystemQueue](../modules/system/system.queue.inc/SystemQueue.md) (class) — Default queue implementation.
- [DrupalQueue::get()](../modules/system/system.queue.inc/DrupalQueue/get.md) (method) — Returns the queue object for a given name.
- [DrupalQueueInterface::claimItem()](../modules/system/system.queue.inc/DrupalQueueInterface/claimItem.md) (method) — Claim an item in the queue for processing.
- [DrupalQueueInterface::createItem()](../modules/system/system.queue.inc/DrupalQueueInterface/createItem.md) (method) — Add a queue item and store it directly to the queue.
- [DrupalQueueInterface::createQueue()](../modules/system/system.queue.inc/DrupalQueueInterface/createQueue.md) (method) — Create a queue.
- [DrupalQueueInterface::deleteItem()](../modules/system/system.queue.inc/DrupalQueueInterface/deleteItem.md) (method) — Delete a finished item from the queue.
- [DrupalQueueInterface::deleteQueue()](../modules/system/system.queue.inc/DrupalQueueInterface/deleteQueue.md) (method) — Delete a queue and every item in the queue.
- [DrupalQueueInterface::numberOfItems()](../modules/system/system.queue.inc/DrupalQueueInterface/numberOfItems.md) (method) — Retrieve the number of items in the queue.
- [DrupalQueueInterface::releaseItem()](../modules/system/system.queue.inc/DrupalQueueInterface/releaseItem.md) (method) — Release an item that the worker could not process, so another worker can come in and process it before the timeout expires.
- [MemoryQueue::__construct()](../modules/system/system.queue.inc/MemoryQueue/__construct.md) (method) — Start working with a queue.
- [MemoryQueue::claimItem()](../modules/system/system.queue.inc/MemoryQueue/claimItem.md) (method)
- [MemoryQueue::createItem()](../modules/system/system.queue.inc/MemoryQueue/createItem.md) (method)
- [MemoryQueue::createQueue()](../modules/system/system.queue.inc/MemoryQueue/createQueue.md) (method)
- [MemoryQueue::deleteItem()](../modules/system/system.queue.inc/MemoryQueue/deleteItem.md) (method)
- [MemoryQueue::deleteQueue()](../modules/system/system.queue.inc/MemoryQueue/deleteQueue.md) (method)
- [MemoryQueue::numberOfItems()](../modules/system/system.queue.inc/MemoryQueue/numberOfItems.md) (method)
- [MemoryQueue::releaseItem()](../modules/system/system.queue.inc/MemoryQueue/releaseItem.md) (method)
- [SystemQueue::__construct()](../modules/system/system.queue.inc/SystemQueue/__construct.md) (method)
- [SystemQueue::claimItem()](../modules/system/system.queue.inc/SystemQueue/claimItem.md) (method)
- [SystemQueue::createItem()](../modules/system/system.queue.inc/SystemQueue/createItem.md) (method)
- [SystemQueue::createQueue()](../modules/system/system.queue.inc/SystemQueue/createQueue.md) (method)
- [SystemQueue::deleteItem()](../modules/system/system.queue.inc/SystemQueue/deleteItem.md) (method)
- [SystemQueue::deleteQueue()](../modules/system/system.queue.inc/SystemQueue/deleteQueue.md) (method)
- [SystemQueue::numberOfItems()](../modules/system/system.queue.inc/SystemQueue/numberOfItems.md) (method)
- [SystemQueue::releaseItem()](../modules/system/system.queue.inc/SystemQueue/releaseItem.md) (method)

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
