# BatchQueue::claimItem()

- **Type:** Method
- **File:** [`includes/batch.queue.inc`](../_file.md), lines 28–35 · [local source](../../../../source/includes/batch.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc#L28-L35)
- **Class:** [BatchQueue](../BatchQueue.md)

## Signature

```php
public function claimItem($lease_time = 0)
```

## Documentation

```text
Overrides SystemQueue::claimItem().

Unlike SystemQueue::claimItem(), this method provides a default lease
time of 0 (no expiration) instead of 30. This allows the item to be
claimed repeatedly until it is deleted.
```

## Code

```php
  public function claimItem($lease_time = 0) {
    $item = db_query_range('SELECT data, item_id FROM {queue} q WHERE name = :name ORDER BY item_id ASC', 0, 1, array(':name' => $this->name))->fetchObject();
    if ($item) {
      $item->data = unserialize($item->data);
      return $item;
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [includes/batch.queue.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
