# _update_7000_user_role_grant_permissions()

- **Type:** Function
- **File:** [`modules/user/user.install`](_file.md), lines 402–415 · [local source](../../../../source/modules/user/user.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install#L402-L415)
- **Module/theme:** user
- **Topics:** [update_api](../../../topics/update_api.md)

## Signature

```php
function _update_7000_user_role_grant_permissions($rid, array $permissions, $module)
```

## Documentation

```text
Utility function: grant a set of permissions to a role during update.

This function is valid for a database schema version 7000.

@param $rid
  The role ID.
@param $permissions
  An array of permissions names.
@param $module
  The name of the module defining the permissions.
@ingroup update_api
```

## Code

```php
function _update_7000_user_role_grant_permissions($rid, array $permissions, $module) {
  // Grant new permissions for the role.
  foreach ($permissions as $name) {
    db_merge('role_permission')
      ->key(array(
        'rid' => $rid,
        'permission' => $name,
      ))
      ->fields(array(
        'module' => $module,
      ))
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/user/user.install](https://github.com/drupal/drupal/blob/7.103/modules/user/user.install) · Licensed GPL-2.0-or-later (see LICENSE)._
