# SystemAuthorizeCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2963–2969 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2963-L2969)
- **Class:** [SystemAuthorizeCase](../SystemAuthorizeCase.md)
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
      'name' => 'Authorize API',
      'description' => 'Tests the authorize.php script and related API.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
