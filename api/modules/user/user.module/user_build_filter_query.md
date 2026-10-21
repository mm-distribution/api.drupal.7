# user_build_filter_query()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3548–3575 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3548-L3575)
- **Module/theme:** user

## Signature

```php
function user_build_filter_query(SelectQuery $query)
```

## Documentation

```text
Extends a query object for user administration filters based on session.

@param $query
  Query object that should be filtered.
```

## Code

```php
function user_build_filter_query(SelectQuery $query) {
  $filters = user_filters();
  // Extend Query with filter conditions.
  foreach (isset($_SESSION['user_overview_filter']) ? $_SESSION['user_overview_filter'] : array() as $filter) {
    list($key, $value) = $filter;
    // This checks to see if this permission filter is an enabled permission for
    // the authenticated role. If so, then all users would be listed, and we can
    // skip adding it to the filter query.
    if ($key == 'permission') {
      $account = new stdClass();
      $account->uid = 'user_filter';
      $account->roles = array(DRUPAL_AUTHENTICATED_RID => 1);
      if (user_access($value, $account)) {
        continue;
      }
      $users_roles_alias = $query->join('users_roles', 'ur', '%alias.uid = u.uid');
      $permission_alias = $query->join('role_permission', 'p', $users_roles_alias . '.rid = %alias.rid');
      $query->condition($permission_alias . '.permission', $value);
    }
    elseif ($key == 'role') {
      $users_roles_alias = $query->join('users_roles', 'ur', '%alias.uid = u.uid');
      $query->condition($users_roles_alias . '.rid' , $value);
    }
    else {
      $query->condition($filters[$key]['field'], $value);
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
