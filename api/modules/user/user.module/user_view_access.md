# user_view_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1609–1627 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1609-L1627)
- **Module/theme:** user

## Signature

```php
function user_view_access($account)
```

## Documentation

```text
User view access callback.

@param $account
  Can either be a full user object or a $uid.
```

## Code

```php
function user_view_access($account) {
  $uid = is_object($account) ? $account->uid : (int) $account;

  // Never allow access to view the anonymous user account.
  if ($uid) {
    // Admins can view all, users can view own profiles at all times.
    if ($GLOBALS['user']->uid == $uid || user_access('administer users')) {
      return TRUE;
    }
    elseif (user_access('access user profiles')) {
      // At this point, load the complete account object.
      if (!is_object($account)) {
        $account = user_load($uid);
      }
      return (is_object($account) && $account->status);
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
