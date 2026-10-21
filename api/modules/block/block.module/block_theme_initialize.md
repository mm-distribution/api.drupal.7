# block_theme_initialize()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 640–659 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L640-L659)
- **Module/theme:** block

## Signature

```php
function block_theme_initialize($theme)
```

## Documentation

```text
Assigns an initial, default set of blocks for a theme.

This function is called the first time a new theme is enabled. The new theme
gets a copy of the default theme's blocks, with the difference that if a
particular region isn't available in the new theme, the block is assigned
to the new theme's default region.

@param $theme
  The name of a theme.
```

## Code

```php
function block_theme_initialize($theme) {
  // Initialize theme's blocks if none already registered.
  $has_blocks = (bool) db_query_range('SELECT 1 FROM {block} WHERE theme = :theme', 0, 1, array(':theme' => $theme))->fetchField();
  if (!$has_blocks) {
    $default_theme = variable_get('theme_default', 'bartik');
    // Apply only to new theme's visible regions.
    $regions = system_region_list($theme, REGIONS_VISIBLE);
    $result = db_query("SELECT * FROM {block} WHERE theme = :theme", array(':theme' => $default_theme), array('fetch' => PDO::FETCH_ASSOC));
    foreach ($result as $block) {
      // If the region isn't supported by the theme, assign the block to the
      // theme's default region.
      if ($block['status'] && !isset($regions[$block['region']])) {
        $block['region'] = system_default_region($theme);
      }
      $block['theme'] = $theme;
      unset($block['bid']);
      drupal_write_record('block', $block);
    }
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
