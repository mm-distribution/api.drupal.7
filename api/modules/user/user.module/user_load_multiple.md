# user_load_multiple()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 290–292 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L290-L292)
- **Module/theme:** user

## Signature

```php
function user_load_multiple($uids = array(), $conditions = array(), $reset = FALSE)
```

## Documentation

```text
Load multiple users based on certain conditions.

This function should be used whenever you need to load more than one user
from the database. Users are loaded into memory and will not require
database access if loaded again during the same page request.

@param $uids
  An array of user IDs.
@param $conditions
  (deprecated) An associative array of conditions on the {users}
  table, where the keys are the database fields and the values are the
  values those fields must have. Instead, it is preferable to use
  EntityFieldQuery to retrieve a list of entity IDs loadable by
  this function.
@param $reset
  A boolean indicating that the internal cache should be reset. Use this if
  loading a user object which has been altered during the page request.

@return
  An array of user objects, indexed by uid.

@see entity_load()
@see user_load()
@see user_load_by_mail()
@see user_load_by_name()
@see EntityFieldQuery

@todo Remove $conditions in Drupal 8.
```

## Code

```php
function user_load_multiple($uids = array(), $conditions = array(), $reset = FALSE) {
  return entity_load('user', $uids, $conditions, $reset);
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
