# MemoryQueue::claimItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 336–345 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L336-L345)
- **Class:** [MemoryQueue](../MemoryQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function claimItem($lease_time = 30)
```

## Documentation

_No docblock in source._

## Code

```php
  public function claimItem($lease_time = 30) {
    foreach ($this->queue as $key => $item) {
      if ($item->expire == 0) {
        $item->expire = time() + $lease_time;
        $this->queue[$key] = $item;
        return $item;
      }
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
