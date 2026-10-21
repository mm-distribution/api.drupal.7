# user_role_load()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3015–3021 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3015-L3021)
- **Module/theme:** user

## Signature

```php
function user_role_load($rid)
```

## Documentation

```text
Fetches a user role by role ID.

@param $rid
  An integer representing the role ID.

@return
  A fully-loaded role object if a role with the given ID exists, or FALSE
  otherwise.

@see user_role_load_by_name()
```

## Code

```php
function user_role_load($rid) {
  return db_select('role', 'r')
    ->fields('r')
    ->condition('rid', $rid)
    ->execute()
    ->fetchObject();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
