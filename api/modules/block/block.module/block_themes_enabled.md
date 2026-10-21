# block_themes_enabled()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 623–627 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L623-L627)
- **Module/theme:** block

## Signature

```php
function block_themes_enabled($theme_list)
```

## Documentation

```text
Initializes blocks for enabled themes.

@param $theme_list
  An array of theme names.
```

## Code

```php
function block_themes_enabled($theme_list) {
  foreach ($theme_list as $theme) {
    block_theme_initialize($theme);
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
