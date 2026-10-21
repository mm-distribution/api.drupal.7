# user_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 807–838 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L807-L838)
- **Module/theme:** user

## Signature

```php
function user_access($string, $account = NULL)
```

## Documentation

```text
Determine whether the user has a given privilege.

@param $string
  The permission, such as "administer nodes", being checked for.
@param $account
  (optional) The account to check, if not given use currently logged in user.

@return
  Boolean TRUE if the user has the requested permission.

All permission checks in Drupal should go through this function. This
way, we guarantee consistent behavior, and ensure that the superuser
can perform all actions.
```

## Code

```php
function user_access($string, $account = NULL) {
  global $user;

  if (!isset($account)) {
    $account = $user;
  }

  // User #1 has all privileges:
  if ($account->uid == 1) {
    return TRUE;
  }

  // To reduce the number of SQL queries, we cache the user's permissions
  // in a static variable.
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['perm'] = &drupal_static(__FUNCTION__);
  }
  $perm = &$drupal_static_fast['perm'];
  if (!isset($perm[$account->uid])) {
    $role_permissions = user_role_permissions($account->roles);

    $perms = array();
    foreach ($role_permissions as $one_role) {
      $perms += $one_role;
    }
    $perm[$account->uid] = $perms;
  }

  return isset($perm[$account->uid][$string]);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
