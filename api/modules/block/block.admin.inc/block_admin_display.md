# block_admin_display()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 23–37 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L23-L37)
- **Module/theme:** block

## Signature

```php
function block_admin_display($theme = NULL)
```

## Documentation

```text
Menu callback for admin/structure/block.

@param $theme
  The theme to display the administration page for. If not provided, defaults
  to the currently used theme.
```

## Code

```php
function block_admin_display($theme = NULL) {
  global $theme_key;

  drupal_theme_initialize();

  if (!isset($theme)) {
    // If theme is not specifically set, rehash for the current theme.
    $theme = $theme_key;
  }

  // Fetch and sort blocks.
  $blocks = block_admin_display_prepare_blocks($theme);

  return drupal_get_form('block_admin_display_form', $blocks, $theme);
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
