# TokenScanTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3050–3056 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3050-L3056)
- **Class:** [TokenScanTest](../TokenScanTest.md)
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
      'name' => 'Token scanning',
      'description' => 'Scan token-like patterns in a dummy text to check token scanning.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
