# block_admin_paths()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 1091–1098 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L1091-L1098)
- **Module/theme:** block
- **Implements:** [hook_admin_paths()](../../system/system.api.php/hook_admin_paths.md)

## Signature

```php
function block_admin_paths()
```

## Documentation

```text
Implements hook_admin_paths().
```

## Code

```php
function block_admin_paths() {
  $paths = array(
    // Exclude the block demonstration page from admin (overlay) treatment.
    // This allows us to present this page in its true form, full page.
    'admin/structure/block/demo/*' => FALSE,
  );
  return $paths;
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
