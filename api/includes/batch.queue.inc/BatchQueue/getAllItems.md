# BatchQueue::getAllItems()

- **Type:** Method
- **File:** [`includes/batch.queue.inc`](../_file.md), lines 42–49 · [local source](../../../../source/includes/batch.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc#L42-L49)
- **Class:** [BatchQueue](../BatchQueue.md)

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
    $items = db_query('SELECT data FROM {queue} q WHERE name = :name ORDER BY item_id ASC', array(':name' => $this->name))->fetchAll();
    foreach ($items as $item) {
      $result[] = unserialize($item->data);
    }
    return $result;
  }
```

---
_Drupal 7.103 · [includes/batch.queue.inc](https://github.com/drupal/drupal/blob/7.103/includes/batch.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
