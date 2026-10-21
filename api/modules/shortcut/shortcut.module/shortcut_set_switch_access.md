# shortcut_set_switch_access()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 268–288 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L268-L288)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_switch_access($account = NULL)
```

## Documentation

```text
Access callback for switching the shortcut set assigned to a user account.

@param object $account
  (optional) The user account whose shortcuts will be switched. If not set,
  permissions will be checked for switching the logged-in user's own
  shortcut set.

@return
  TRUE if the current user has access to switch the shortcut set of the
  provided account, FALSE otherwise.
```

## Code

```php
function shortcut_set_switch_access($account = NULL) {
  global $user;

  if (user_access('administer shortcuts')) {
    // Administrators can switch anyone's shortcut set.
    return TRUE;
  }

  if (!user_access('switch shortcut sets')) {
    // The user has no permission to switch anyone's shortcut set.
    return FALSE;
  }

  if (!isset($account) || $user->uid == $account->uid) {
    // Users with the 'switch shortcut sets' permission can switch their own
    // shortcuts sets.
    return TRUE;
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
