# user_has_role()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 870–876 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L870-L876)
- **Module/theme:** user

## Signature

```php
function user_has_role($rid, $account = NULL)
```

## Documentation

```text
Checks if a user has a role.

@param int $rid
  A role ID.

@param object|null $account
  (optional) A user account. Defaults to the current user.

@return bool
  TRUE if the user has the role, or FALSE if not.
```

## Code

```php
function user_has_role($rid, $account = NULL) {
  if (!$account) {
    $account = $GLOBALS['user'];
  }

  return isset($account->roles[$rid]);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
