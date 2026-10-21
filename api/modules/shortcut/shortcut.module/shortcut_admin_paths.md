# shortcut_admin_paths()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 167–172 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L167-L172)
- **Module/theme:** shortcut
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function shortcut_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function shortcut_admin_paths() {
  $paths = array(
    'user/*/shortcuts' => TRUE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
