# user_permission_get_modules()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3141–3150 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3141-L3150)
- **Module/theme:** user

## Signature

```php
function user_permission_get_modules()
```

## Documentation

```text
Determine the modules that permissions belong to.

@return
  An associative array in the format $permission => $module.
```

## Code

```php
function user_permission_get_modules() {
  $permissions = array();
  foreach (module_implements('permission') as $module) {
    $perms = module_invoke($module, 'permission');
    foreach ($perms as $key => $value) {
      $permissions[$key] = $module;
    }
  }
  return $permissions;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
