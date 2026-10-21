# BatchMemoryQueue::getAllItems()

- **Type:** Method
- **File:** [`includes/batch.queue.inc`](../_file.md), lines 77–83 · [local source](../../../../source/includes/batch.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc#L77-L83)
- **Class:** [BatchMemoryQueue](../BatchMemoryQueue.md)

## Signature

```php
public function getAllItems()
```

## Documentation

```text
Retrieves all remaining items in the queue.

This is specific to Batch API and is not part of the DrupalQueueInterface.
```

## Code

```php
  public function getAllItems() {
    $result = array();
    foreach ($this->queue as $item) {
      $result[] = $item->data;
    }
    return $result;
  }
```

---
_Drupal 7.103 · [includes/batch.queue.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
