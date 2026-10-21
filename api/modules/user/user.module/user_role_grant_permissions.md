# user_role_grant_permissions()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3205–3223 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3205-L3223)
- **Module/theme:** user

## Signature

```php
function user_role_grant_permissions($rid, array $permissions = array())
```

## Documentation

```text
Grant permissions to a user role.

@param $rid
  The ID of a user role to alter.
@param $permissions
  A list of permission names to grant.

@see user_role_change_permissions()
@see user_role_revoke_permissions()
```

## Code

```php
function user_role_grant_permissions($rid, array $permissions = array()) {
  $modules = user_permission_get_modules();
  // Grant new permissions for the role.
  foreach ($permissions as $name) {
    db_merge('role_permission')
      ->key(array(
        'rid' => $rid,
        'permission' => $name,
      ))
      ->fields(array(
        'module' => $modules[$name],
      ))
      ->execute();
  }

  // Clear the user access cache.
  drupal_static_reset('user_access');
  drupal_static_reset('user_role_permissions');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
