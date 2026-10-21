# UserAdminTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1777–1783 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1777-L1783)
- **Class:** [UserAdminTestCase](../UserAdminTestCase.md)
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
      'name' => 'User administration',
      'description' => 'Test user administration page functionality.',
      'group' => 'User'
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
