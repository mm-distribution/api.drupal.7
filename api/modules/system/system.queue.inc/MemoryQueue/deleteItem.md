# MemoryQueue::deleteItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 347–349 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L347-L349)
- **Class:** [MemoryQueue](../MemoryQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function deleteItem($item)
```

## Documentation

_No docblock in source._

## Code

```php
  public function deleteItem($item) {
    unset($this->queue[$item->item_id]);
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
