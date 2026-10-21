# translation_admin_paths()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 96–103 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L96-L103)
- **Module/theme:** translation
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function translation_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function translation_admin_paths() {
  if (variable_get('node_admin_theme')) {
    $paths = array(
      'node/*/translate' => TRUE,
    );
    return $paths;
  }
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
