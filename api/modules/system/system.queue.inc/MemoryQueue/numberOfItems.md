# MemoryQueue::numberOfItems()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 332–334 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L332-L334)
- **Class:** [MemoryQueue](../MemoryQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function numberOfItems()
```

## Documentation

_No docblock in source._

## Code

```php
  public function numberOfItems() {
    return count($this->queue);
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
