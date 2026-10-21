# taxonomy_admin_paths()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 365–370 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L365-L370)
- **Module/theme:** taxonomy
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function taxonomy_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function taxonomy_admin_paths() {
  $paths = array(
    'taxonomy/term/*/edit' => TRUE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
