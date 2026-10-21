# user_role_delete()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3092–3121 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3092-L3121)
- **Module/theme:** user

## Signature

```php
function user_role_delete($role)
```

## Documentation

```text
Delete a user role from database.

@param $role
  A string with the role name, or an integer with the role ID.
```

## Code

```php
function user_role_delete($role) {
  if (is_int($role)) {
    $role = user_role_load($role);
  }
  else {
    $role = user_role_load_by_name($role);
  }

  // If this is the administrator role, delete the user_admin_role variable.
  if ($role->rid == variable_get('user_admin_role')) {
    variable_del('user_admin_role');
  }

  db_delete('role')
    ->condition('rid', $role->rid)
    ->execute();
  db_delete('role_permission')
    ->condition('rid', $role->rid)
    ->execute();
  // Update the users who have this role set:
  db_delete('users_roles')
    ->condition('rid', $role->rid)
    ->execute();

  module_invoke_all('user_role_delete', $role);

  // Clear the user access cache.
  drupal_static_reset('user_access');
  drupal_static_reset('user_role_permissions');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
