# user_cancel_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1642–1644 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1642-L1644)
- **Module/theme:** user

## Signature

```php
function user_cancel_access($account)
```

## Documentation

```text
Menu access callback; limit access to account cancellation pages.

Limit access to users with the 'cancel account' permission or administrative
users, and prevent the anonymous user from cancelling the account.
```

## Code

```php
function user_cancel_access($account) {
  return ((($GLOBALS['user']->uid == $account->uid) && user_access('cancel account')) || user_access('administer users')) && $account->uid > 0;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
