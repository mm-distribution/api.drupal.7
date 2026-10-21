# SystemThemeFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1902–1908 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1902-L1908)
- **Class:** [SystemThemeFunctionalTest](../SystemThemeFunctionalTest.md)
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
      'name' => 'Theme interface functionality',
      'description' => 'Tests the theme interface functionality by enabling and switching themes, and using an administration theme.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
