# user_role_revoke_permissions()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3236–3246 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3236-L3246)
- **Module/theme:** user

## Signature

```php
function user_role_revoke_permissions($rid, array $permissions = array())
```

## Documentation

```text
Revoke permissions from a user role.

@param $rid
  The ID of a user role to alter.
@param $permissions
  A list of permission names to revoke.

@see user_role_change_permissions()
@see user_role_grant_permissions()
```

## Code

```php
function user_role_revoke_permissions($rid, array $permissions = array()) {
  // Revoke permissions for the role.
  db_delete('role_permission')
    ->condition('rid', $rid)
    ->condition('permission', $permissions, 'IN')
    ->execute();

  // Clear the user access cache.
  drupal_static_reset('user_access');
  drupal_static_reset('user_role_permissions');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
