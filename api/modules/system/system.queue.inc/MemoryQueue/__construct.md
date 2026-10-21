# MemoryQueue::__construct()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 317–320 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L317-L320)
- **Class:** [MemoryQueue](../MemoryQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function __construct($name)
```

## Documentation

```text
Start working with a queue.

@param $name
  Arbitrary string. The name of the queue to work with.
```

## Code

```php
  public function __construct($name) {
    $this->queue = array();
    $this->id_sequence = 0;
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
