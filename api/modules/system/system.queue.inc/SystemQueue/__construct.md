# SystemQueue::__construct()

- **Type:** Method
- **File:** [`modules/system/system.queue.inc`](../_file.md), lines 206–208 · [local source](../../../../../source/modules/system/system.queue.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc#L206-L208)
- **Class:** [SystemQueue](../SystemQueue.md)
- **Module/theme:** system
- **Topics:** [queue](../../../../topics/queue.md)

## Signature

```php
public function __construct($name)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct($name) {
    $this->name = $name;
  }
```

---
_Drupal 7.103 · [modules/system/system.queue.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.queue.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
