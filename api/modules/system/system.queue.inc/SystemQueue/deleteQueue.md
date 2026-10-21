# SystemQueue::deleteQueue()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 282–286 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L282-L286)
- **Class:** [SystemQueue](../SystemQueue.md)
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
    db_delete('queue')
      ->condition('name', $this->name)
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
