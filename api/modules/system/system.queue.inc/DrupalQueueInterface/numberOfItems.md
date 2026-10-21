# DrupalQueueInterface::numberOfItems()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 128–128 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L128)
- **Class:** [DrupalQueueInterface](../DrupalQueueInterface.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function numberOfItems();
```

## Documentation

```text
Retrieve the number of items in the queue.

This is intended to provide a "best guess" count of the number of items in
the queue. Depending on the implementation and the setup, the accuracy of
the results of this function may vary.

e.g. On a busy system with a large number of consumers and items, the
result might only be valid for a fraction of a second and not provide an
accurate representation.

@return
  An integer estimate of the number of items in the queue.
```

## Code

```php
  public function numberOfItems();
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
