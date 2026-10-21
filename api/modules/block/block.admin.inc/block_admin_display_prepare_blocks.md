# block_admin_display_prepare_blocks()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 51–57 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L51-L57)
- **Module/theme:** block

## Signature

```php
function block_admin_display_prepare_blocks($theme)
```

## Documentation

```text
Prepares a list of blocks for display on the blocks administration page.

@param $theme
  The machine-readable name of the theme whose blocks should be returned.

@return
  An array of blocks, as returned by _block_rehash(), sorted by region in
  preparation for display on the blocks administration page.

@see block_admin_display_form()
```

## Code

```php
function block_admin_display_prepare_blocks($theme) {
  $blocks = _block_rehash($theme);
  $compare_theme = &drupal_static('_block_compare:theme');
  $compare_theme = $theme;
  usort($blocks, '_block_compare');
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
