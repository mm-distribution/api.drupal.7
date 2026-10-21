# DrupalQueueInterface::createItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 112–112 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L112)
- **Class:** [DrupalQueueInterface](../DrupalQueueInterface.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function createItem($data);
```

## Documentation

```text
Add a queue item and store it directly to the queue.

@param $data
  Arbitrary data to be associated with the new task in the queue.
@return
  TRUE if the item was successfully created and was (best effort) added
  to the queue, otherwise FALSE. We don't guarantee the item was
  committed to disk etc, but as far as we know, the item is now in the
  queue.
```

## Code

```php
  public function createItem($data);
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
