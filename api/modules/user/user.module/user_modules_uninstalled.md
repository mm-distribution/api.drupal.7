# user_modules_uninstalled()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 4075–4079 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L4075-L4079)
- **Module/theme:** user
- **Implements:** [hook_modules_uninstalled()](../../system/system.api.php/hook_modules_uninstalled.md)

## Signature

```php
function user_modules_uninstalled($modules)
```

## Documentation

```text
Implements hook_modules_uninstalled().
```

## Code

```php
function user_modules_uninstalled($modules) {
   db_delete('role_permission')
     ->condition('module', $modules, 'IN')
     ->execute();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
