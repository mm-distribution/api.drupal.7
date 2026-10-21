# DrupalQueueInterface

- **Type:** Interface
- **File:** [`modules/system/system.queue.inc`](_file.md), lines 99–184 · [local source](../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L99-L184)
- **Module/theme:** system
- **Topics:** [queue](../../../topics/queue.md)

## Signature

```php
interface DrupalQueueInterface
```

## Documentation

_No docblock in source._

## Methods (derived index)

- [createItem()](DrupalQueueInterface/createItem.md) — Add a queue item and store it directly to the queue.
- [numberOfItems()](DrupalQueueInterface/numberOfItems.md) — Retrieve the number of items in the queue.
- [claimItem()](DrupalQueueInterface/claimItem.md) — Claim an item in the queue for processing.
- [deleteItem()](DrupalQueueInterface/deleteItem.md) — Delete a finished item from the queue.
- [releaseItem()](DrupalQueueInterface/releaseItem.md) — Release an item that the worker could not process, so another worker can come in and process it before the timeout expires.
- [createQueue()](DrupalQueueInterface/createQueue.md) — Create a queue.
- [deleteQueue()](DrupalQueueInterface/deleteQueue.md) — Delete a queue and every item in the queue.

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
