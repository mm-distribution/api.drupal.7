# UserPermissionsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1682–1688 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1682-L1688)
- **Class:** [UserPermissionsTestCase](../UserPermissionsTestCase.md)
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
      'name' => 'Role permissions',
      'description' => 'Verify that role permissions can be added and removed via the permissions page.',
      'group' => 'User'
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
