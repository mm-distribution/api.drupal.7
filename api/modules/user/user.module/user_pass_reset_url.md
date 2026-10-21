# user_pass_reset_url()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2401–2404 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2401-L2404)
- **Module/theme:** user

## Signature

```php
function user_pass_reset_url($account)
```

## Documentation

```text
Generates a unique URL for a user to login and reset their password.

@param object $account
  An object containing the user account, which must contain at least the
  following properties:
  - uid: The user ID number.
  - login: The UNIX timestamp of the user's last login.

@return
  A unique URL that provides a one-time log in for the user, from which
  they can change their password.
```

## Code

```php
function user_pass_reset_url($account) {
  $timestamp = REQUEST_TIME;
  return url("user/reset/$account->uid/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail), array('absolute' => TRUE));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
