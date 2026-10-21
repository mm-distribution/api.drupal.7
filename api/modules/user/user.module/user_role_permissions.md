# user_role_permissions()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 756–790 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L756-L790)
- **Module/theme:** user

## Signature

```php
function user_role_permissions($roles = array())
```

## Documentation

```text
Determine the permissions for one or more roles.

@param $roles
  An array whose keys are the role IDs of interest, such as $user->roles.

@return
  If $roles is a non-empty array, an array indexed by role ID is returned.
  Each value is an array whose keys are the permission strings for the given
  role ID. If $roles is empty nothing is returned.
```

## Code

```php
function user_role_permissions($roles = array()) {
  $cache = &drupal_static(__FUNCTION__, array());

  $role_permissions = $fetch = array();

  if ($roles) {
    foreach ($roles as $rid => $name) {
      if (isset($cache[$rid])) {
        $role_permissions[$rid] = $cache[$rid];
      }
      else {
        // Add this rid to the list of those needing to be fetched.
        $fetch[] = $rid;
        // Prepare in case no permissions are returned.
        $cache[$rid] = array();
      }
    }

    if ($fetch) {
      // Get from the database permissions that were not in the static variable.
      // Only role IDs with at least one permission assigned will return rows.
      $result = db_query("SELECT rid, permission FROM {role_permission} WHERE rid IN (:fetch)", array(':fetch' => $fetch));

      foreach ($result as $row) {
        $cache[$row->rid][$row->permission] = TRUE;
      }
      foreach ($fetch as $rid) {
        // For every rid, we know we at least assigned an empty array.
        $role_permissions[$rid] = $cache[$rid];
      }
    }
  }

  return $role_permissions;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
