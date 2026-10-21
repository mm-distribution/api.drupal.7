# UserEditedOwnAccountTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2524–2530 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2524-L2530)
- **Class:** [UserEditedOwnAccountTestCase](../UserEditedOwnAccountTestCase.md)
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
      'name' => 'User edited own account',
      'description' => 'Test user edited own account can still log in.',
      'group' => 'User',
    );
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
