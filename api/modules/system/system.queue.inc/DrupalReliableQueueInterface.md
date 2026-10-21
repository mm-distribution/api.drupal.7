# DrupalReliableQueueInterface

- **Type:** Interface
- **File:** [`modules/system/system.queue.inc`](_file.md), lines 192–193 · [local source](../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L192-L193)
- **Module/theme:** system
- **Topics:** [queue](../../../topics/queue.md)

## Signature

```php
interface DrupalReliableQueueInterface extends DrupalQueueInterface
```

## Documentation

```text
Reliable queue interface.

Classes implementing this interface preserve the order of messages and
guarantee that every item will be executed at least once.
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
