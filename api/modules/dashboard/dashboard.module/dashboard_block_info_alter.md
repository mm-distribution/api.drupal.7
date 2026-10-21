# dashboard_block_info_alter()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 101–115 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L101-L115)
- **Module/theme:** dashboard
- **Implements:** [hook_block_info_alter()](../../block/block.api.php/hook_block_info_alter.md)

## Signature

```php
function dashboard_block_info_alter(&$blocks, $theme, $code_blocks)
```

## Documentation

```text
Implements hook_block_info_alter().
```

## Code

```php
function dashboard_block_info_alter(&$blocks, $theme, $code_blocks) {
  $admin_theme = variable_get('admin_theme');
  if (($admin_theme && $theme == $admin_theme) || (!$admin_theme && $theme == variable_get('theme_default', 'bartik'))) {
    foreach ($blocks as $module => &$module_blocks) {
      foreach ($module_blocks as $delta => &$block) {
        // Make administrative blocks that are not already in use elsewhere
        // available for the dashboard.
        if (empty($block['status']) && (empty($block['region']) || $block['region'] == BLOCK_REGION_NONE) && !empty($code_blocks[$module][$delta]['properties']['administrative'])) {
          $block['status'] = 1;
          $block['region'] = 'dashboard_inactive';
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
