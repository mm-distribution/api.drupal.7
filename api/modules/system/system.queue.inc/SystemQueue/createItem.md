# SystemQueue::createItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 210–222 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L210-L222)
- **Class:** [SystemQueue](../SystemQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function createItem($data)
```

## Documentation

_No docblock in source._

## Code

```php
  public function createItem($data) {
    // During a Drupal 6.x to 7.x update, drupal_get_schema() does not contain
    // the queue table yet, so we cannot rely on drupal_write_record().
    $query = db_insert('queue')
      ->fields(array(
        'name' => $this->name,
        'data' => serialize($data),
        // We cannot rely on REQUEST_TIME because many items might be created
        // by a single request which takes longer than 1 second.
        'created' => time(),
      ));
    return (bool) $query->execute();
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
