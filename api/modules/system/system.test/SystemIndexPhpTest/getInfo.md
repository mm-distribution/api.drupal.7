# SystemIndexPhpTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3016–3022 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3016-L3022)
- **Class:** [SystemIndexPhpTest](../SystemIndexPhpTest.md)
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
      'name' => 'Index.php handling',
      'description' => "Test the handling of requests containing 'index.php'.",
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
