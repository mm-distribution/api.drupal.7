# user_load_by_mail()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 381–384 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L381-L384)
- **Module/theme:** user

## Signature

```php
function user_load_by_mail($mail)
```

## Documentation

```text
Fetch a user object by email address.

@param $mail
  String with the account's e-mail address.
@return
  A fully-loaded $user object upon successful user load or FALSE if user
  cannot be loaded.

@see user_load_multiple()
```

## Code

```php
function user_load_by_mail($mail) {
  $users = user_load_multiple(array(), array('mail' => $mail));
  return reset($users);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
