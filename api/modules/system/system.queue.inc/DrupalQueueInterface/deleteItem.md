# DrupalQueueInterface::deleteItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 156–156 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L156)
- **Class:** [DrupalQueueInterface](../DrupalQueueInterface.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function deleteItem($item);
```

## Documentation

```text
Delete a finished item from the queue.

@param $item
  The item returned by DrupalQueueInterface::claimItem().
```

## Code

```php
  public function deleteItem($item);
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
