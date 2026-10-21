# QueueTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2120–2126 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2120-L2126)
- **Class:** [QueueTestCase](../QueueTestCase.md)
- **Module/theme:** system

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Queue functionality',
      'description' => 'Queues and dequeues a set of items to check the basic queue functionality.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
