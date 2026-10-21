# user_register_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1599–1601 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1599-L1601)
- **Module/theme:** user

## Signature

```php
function user_register_access()
```

## Documentation

```text
Determines if the current user has access to the user registration page.

@return bool
  TRUE if the user is not already logged in and can register for an account.
```

## Code

```php
function user_register_access() {
  return user_is_anonymous() && variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
