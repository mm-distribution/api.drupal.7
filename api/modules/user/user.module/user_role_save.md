# user_role_save()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3055–3084 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3055-L3084)
- **Module/theme:** user

## Signature

```php
function user_role_save($role)
```

## Documentation

```text
Save a user role to the database.

@param $role
  A role object to modify or add. If $role->rid is not specified, a new
  role will be created.
@return
  Status constant indicating if role was created or updated.
  Failure to write the user role record will return FALSE. Otherwise.
  SAVED_NEW or SAVED_UPDATED is returned depending on the operation
  performed.
```

## Code

```php
function user_role_save($role) {
  if ($role->name) {
    // Prevent leading and trailing spaces in role names.
    $role->name = trim($role->name);
  }
  if (!isset($role->weight)) {
    // Set a role weight to make this new role last.
    $query = db_select('role');
    $query->addExpression('MAX(weight)');
    $role->weight = $query->execute()->fetchField() + 1;
  }

  // Let modules modify the user role before it is saved to the database.
  module_invoke_all('user_role_presave', $role);

  if (!empty($role->rid) && $role->name) {
    $status = drupal_write_record('role', $role, 'rid');
    module_invoke_all('user_role_update', $role);
  }
  else {
    $status = drupal_write_record('role', $role);
    module_invoke_all('user_role_insert', $role);
  }

  // Clear the user access cache.
  drupal_static_reset('user_access');
  drupal_static_reset('user_role_permissions');

  return $status;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
