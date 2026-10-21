# MemoryQueue::deleteQueue()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 363–366 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L363-L366)
- **Class:** [MemoryQueue](../MemoryQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function deleteQueue()
```

## Documentation

_No docblock in source._

## Code

```php
  public function deleteQueue() {
    $this->queue = array();
    $this->id_sequence = 0;
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
