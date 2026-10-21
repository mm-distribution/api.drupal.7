# user_role_load_by_name()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3035–3041 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3035-L3041)
- **Module/theme:** user

## Signature

```php
function user_role_load_by_name($role_name)
```

## Documentation

```text
Fetches a user role by role name.

@param $role_name
  A string representing the role name.

@return
  A fully-loaded role object if a role with the given name exists, or FALSE
  otherwise.

@see user_role_load()
```

## Code

```php
function user_role_load_by_name($role_name) {
  return db_select('role', 'r')
    ->fields('r')
    ->condition('name', $role_name)
    ->execute()
    ->fetchObject();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
