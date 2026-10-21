# ShutdownFunctionsTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2784–2790 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2784-L2790)
- **Class:** [ShutdownFunctionsTest](../ShutdownFunctionsTest.md)
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
      'name' => 'Shutdown functions',
      'description' => 'Functional tests for shutdown functions',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
