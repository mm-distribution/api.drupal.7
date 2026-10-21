# user_roles()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 2971–3001 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L2971-L3001)
- **Module/theme:** user

## Signature

```php
function user_roles($membersonly = FALSE, $permission = NULL)
```

## Documentation

```text
Retrieve an array of roles matching specified conditions.

@param $membersonly
  Set this to TRUE to exclude the 'anonymous' role.
@param $permission
  A string containing a permission. If set, only roles containing that
  permission are returned.

@return
  An associative array with the role id as the key and the role name as
  value.
```

## Code

```php
function user_roles($membersonly = FALSE, $permission = NULL) {
  $query = db_select('role', 'r');
  $query->addTag('translatable');
  $query->fields('r', array('rid', 'name'));
  $query->orderBy('weight');
  $query->orderBy('name');
  if (!empty($permission)) {
    $query->innerJoin('role_permission', 'p', 'r.rid = p.rid');
    $query->condition('p.permission', $permission);
  }
  $result = $query->execute();

  $roles = array();
  foreach ($result as $role) {
    switch ($role->rid) {
      // We only translate the built in role names
      case DRUPAL_ANONYMOUS_RID:
        if (!$membersonly) {
          $roles[$role->rid] = t($role->name);
        }
        break;
      case DRUPAL_AUTHENTICATED_RID:
        $roles[$role->rid] = t($role->name);
        break;
      default:
        $roles[$role->rid] = $role->name;
    }
  }

  return $roles;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
