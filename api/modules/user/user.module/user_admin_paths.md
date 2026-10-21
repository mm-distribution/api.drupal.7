# user_admin_paths()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1959–1966 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1959-L1966)
- **Module/theme:** user
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function user_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function user_admin_paths() {
  $paths = array(
    'user/*/cancel' => TRUE,
    'user/*/edit' => TRUE,
    'user/*/edit/*' => TRUE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
