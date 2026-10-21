# user_modules_installed()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4056–4070 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4056-L4070)
- **Module/theme:** user
- **Implements:** [hook_modules_installed()](../../system/system.api.php/hook_modules_installed.md)

## Signature

```php
function user_modules_installed($modules)
```

## Documentation

```text
Implements hook_modules_installed().
```

## Code

```php
function user_modules_installed($modules) {
  // Assign all available permissions to the administrator role.
  $rid = variable_get('user_admin_role', 0);
  if ($rid) {
    $permissions = array();
    foreach ($modules as $module) {
      if ($module_permissions = module_invoke($module, 'permission')) {
        $permissions = array_merge($permissions, array_keys($module_permissions));
      }
    }
    if (!empty($permissions)) {
      user_role_grant_permissions($rid, $permissions);
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
