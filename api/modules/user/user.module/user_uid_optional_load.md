# user_uid_optional_load()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1992–1997 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1992-L1997)
- **Module/theme:** user

## Signature

```php
function user_uid_optional_load($uid = NULL)
```

## Documentation

```text
Load either a specified or the current user account.

@param $uid
  An optional user ID of the user to load. If not provided, the current
  user's ID will be used.
@return
  A fully-loaded $user object upon successful user load, FALSE if user
  cannot be loaded.

@see user_load()
@todo rethink the naming of this in Drupal 8.
```

## Code

```php
function user_uid_optional_load($uid = NULL) {
  if (!isset($uid)) {
    $uid = $GLOBALS['user']->uid;
  }
  return user_load($uid);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
