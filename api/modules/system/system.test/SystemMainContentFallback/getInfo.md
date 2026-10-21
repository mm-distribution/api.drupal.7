# SystemMainContentFallback::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1818–1824 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1818-L1824)
- **Class:** [SystemMainContentFallback](../SystemMainContentFallback.md)
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
      'name' => 'Main content rendering fallback',
      'description' => ' Test system module main content rendering fallback.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
