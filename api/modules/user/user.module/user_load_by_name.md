# user_load_by_name()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 397–400 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L397-L400)
- **Module/theme:** user

## Signature

```php
function user_load_by_name($name)
```

## Documentation

```text
Fetch a user object by account name.

@param $name
  String with the account's user name.
@return
  A fully-loaded $user object upon successful user load or FALSE if user
  cannot be loaded.

@see user_load_multiple()
```

## Code

```php
function user_load_by_name($name) {
  $users = user_load_multiple(array(), array('name' => $name));
  return reset($users);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
