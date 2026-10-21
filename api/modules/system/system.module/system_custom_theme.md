# system_custom_theme()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1990–1994 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1990-L1994)
- **Module/theme:** system
- **Implements:** [hook_custom_theme()](../system.api.php/hook_custom_theme.md)

## Signature

```php
function system_custom_theme()
```

## Documentation

```text
Implements hook_custom_theme().
```

## Code

```php
function system_custom_theme() {
  if (user_access('view the administration theme') && path_is_admin(current_path())) {
    return variable_get('admin_theme');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
