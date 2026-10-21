# SystemQueue::deleteItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 270–274 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L270-L274)
- **Class:** [SystemQueue](../SystemQueue.md)
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
    db_delete('queue')
      ->condition('item_id', $item->item_id)
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
