# DrupalQueueInterface::releaseItem()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 165–165 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L165)
- **Class:** [DrupalQueueInterface](../DrupalQueueInterface.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function releaseItem($item);
```

## Documentation

```text
Release an item that the worker could not process, so another
worker can come in and process it before the timeout expires.

@param $item
@return boolean
```

## Code

```php
  public function releaseItem($item);
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
