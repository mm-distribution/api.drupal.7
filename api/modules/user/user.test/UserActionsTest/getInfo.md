# UserActionsTest::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 3008–3014 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L3008-L3014)
- **Class:** [UserActionsTest](../UserActionsTest.md)
- **Module/theme:** user

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
      'name' => 'User actions',
      'description' => 'Test actions provided by the user module.',
      'group' => 'User',
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
