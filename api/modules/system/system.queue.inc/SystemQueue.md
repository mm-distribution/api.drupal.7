# SystemQueue

- **Type:** Class
- **File:** [`modules/system/system.queue.inc`](_file.md), lines 198–287 · [local source](../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L198-L287)
- **Module/theme:** system
- **Topics:** [queue](../../../topics/queue.md)

## Signature

```php
class SystemQueue implements DrupalReliableQueueInterface
```

## Documentation

```text
Default queue implementation.
```

## Properties

### $name

```php
protected $name;
```

```text
The name of the queue this instance is working with.

@var string
```

## Methods (derived index)

- [__construct()](SystemQueue/__construct.md)
- [createItem()](SystemQueue/createItem.md)
- [numberOfItems()](SystemQueue/numberOfItems.md)
- [claimItem()](SystemQueue/claimItem.md)
- [releaseItem()](SystemQueue/releaseItem.md)
- [deleteItem()](SystemQueue/deleteItem.md)
- [createQueue()](SystemQueue/createQueue.md)
- [deleteQueue()](SystemQueue/deleteQueue.md)

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
