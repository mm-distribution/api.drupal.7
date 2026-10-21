# system_admin_paths()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4094–4104 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4094-L4104)
- **Module/theme:** system
- **Implements:** [hook_admin_paths()](../system.api.php/hook_admin_paths.md)

## Signature

```php
function system_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function system_admin_paths() {
  $paths = array(
    'admin' => TRUE,
    'admin/*' => TRUE,
    'batch' => TRUE,
    // This page should not be treated as administrative since it outputs its
    // own content (outside of any administration theme).
    'admin/reports/status/php' => FALSE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
