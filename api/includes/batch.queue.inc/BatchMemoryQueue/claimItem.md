# BatchMemoryQueue::claimItem()

- **Type:** Method
- **File:** [`includes/batch.queue.inc`](../_file.md), lines 64–70 · [local source](../../../../source/includes/batch.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc#L64-L70)
- **Class:** [BatchMemoryQueue](../BatchMemoryQueue.md)

## Signature

```php
public function claimItem($lease_time = 0)
```

## Documentation

```text
Overrides MemoryQueue::claimItem().

Unlike MemoryQueue::claimItem(), this method provides a default lease
time of 0 (no expiration) instead of 30. This allows the item to be
claimed repeatedly until it is deleted.
```

## Code

```php
  public function claimItem($lease_time = 0) {
    if (!empty($this->queue)) {
      reset($this->queue);
      return current($this->queue);
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/batch.queue.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
