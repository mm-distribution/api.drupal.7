# user_role_edit_access()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3126–3133 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3126-L3133)
- **Module/theme:** user

## Signature

```php
function user_role_edit_access($role)
```

## Documentation

```text
Menu access callback for user role editing.
```

## Code

```php
function user_role_edit_access($role) {
  // Prevent the system-defined roles from being altered or removed.
  if ($role->rid == DRUPAL_ANONYMOUS_RID || $role->rid == DRUPAL_AUTHENTICATED_RID) {
    return FALSE;
  }

  return user_access('administer permissions');
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
