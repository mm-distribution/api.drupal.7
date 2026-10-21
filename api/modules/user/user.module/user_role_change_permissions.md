# user_role_change_permissions()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3181–3192 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3181-L3192)
- **Module/theme:** user

## Signature

```php
function user_role_change_permissions($rid, array $permissions = array())
```

## Documentation

```text
Change permissions for a user role.

This function may be used to grant and revoke multiple permissions at once.
For example, when a form exposes checkboxes to configure permissions for a
role, the form submit handler may directly pass the submitted values for the
checkboxes form element to this function.

@param $rid
  The ID of a user role to alter.
@param $permissions
  An associative array, where the key holds the permission name and the value
  determines whether to grant or revoke that permission. Any value that
  evaluates to TRUE will cause the permission to be granted. Any value that
  evaluates to FALSE will cause the permission to be revoked.
  @code
    array(
      'administer nodes' => 0,                // Revoke 'administer nodes'
      'administer blocks' => FALSE,           // Revoke 'administer blocks'
      'access user profiles' => 1,            // Grant 'access user profiles'
      'access content' => TRUE,               // Grant 'access content'
      'access comments' => 'access comments', // Grant 'access comments'
    )
  @endcode
  Existing permissions are not changed, unless specified in $permissions.

@see user_role_grant_permissions()
@see user_role_revoke_permissions()
```

## Code

```php
function user_role_change_permissions($rid, array $permissions = array()) {
  // Grant new permissions for the role.
  $grant = array_filter($permissions);
  if (!empty($grant)) {
    user_role_grant_permissions($rid, array_keys($grant));
  }
  // Revoke permissions for the role.
  $revoke = array_diff_assoc($permissions, $grant);
  if (!empty($revoke)) {
    user_role_revoke_permissions($rid, array_keys($revoke));
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
