# user_cancel_url()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2423–2426 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2423-L2426)
- **Module/theme:** user

## Signature

```php
function user_cancel_url($account)
```

## Documentation

```text
Generates a URL to confirm an account cancellation request.

@param object $account
  The user account object, which must contain at least the following
  properties:
  - uid: The user ID number.
  - pass: The hashed user password string.
  - login: The UNIX timestamp of the user's last login.

@return
  A unique URL that may be used to confirm the cancellation of the user
  account.

@see user_mail_tokens()
@see user_cancel_confirm()
```

## Code

```php
function user_cancel_url($account) {
  $timestamp = REQUEST_TIME;
  return url("user/$account->uid/cancel/confirm/$timestamp/" . user_pass_rehash($account->pass, $timestamp, $account->login, $account->uid, $account->mail), array('absolute' => TRUE));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
