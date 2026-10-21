# block_admin_demo()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 11–14 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L11-L14)
- **Module/theme:** block

## Signature

```php
function block_admin_demo($theme = NULL)
```

## Documentation

```text
Menu callback for admin/structure/block/demo.
```

## Code

```php
function block_admin_demo($theme = NULL) {
  drupal_add_css(drupal_get_path('module', 'block') . '/block.css');
  return '';
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
