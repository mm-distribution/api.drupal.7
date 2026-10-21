# SystemQueue::releaseItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 261–268 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L261-L268)
- **Class:** [SystemQueue](../SystemQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function releaseItem($item)
```

## Documentation

_No docblock in source._

## Code

```php
  public function releaseItem($item) {
    $update = db_update('queue')
      ->fields(array(
        'expire' => 0,
      ))
      ->condition('item_id', $item->item_id);
      return $update->execute();
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
