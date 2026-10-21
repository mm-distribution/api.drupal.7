# SystemValidTokenTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3088–3094 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3088-L3094)
- **Class:** [SystemValidTokenTest](../SystemValidTokenTest.md)
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
      'name' => 'Token validation',
      'description' => 'Test the security token validation.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
