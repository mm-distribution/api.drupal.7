# _block_themes_access()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 183–185 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L183-L185)
- **Module/theme:** block

## Signature

```php
function _block_themes_access($theme)
```

## Documentation

```text
Menu item access callback - only admin or enabled themes can be accessed.
```

## Code

```php
function _block_themes_access($theme) {
  return user_access('administer blocks') && drupal_theme_access($theme);
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
