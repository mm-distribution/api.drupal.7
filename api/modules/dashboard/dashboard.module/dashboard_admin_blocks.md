# dashboard_admin_blocks()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 315–336 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L315-L336)
- **Module/theme:** dashboard

## Signature

```php
function dashboard_admin_blocks()
```

## Documentation

```text
Page callback: Builds the page for administering dashboard blocks.

This page reuses the Block module's administration form but limits editing
to blocks that are available to appear on the dashboard.

@see block_admin_display()
@see block_admin_display_form()
@see dashboard_form_dashboard_admin_display_form_alter()
@see template_preprocess_dashboard_admin_display_form()
```

## Code

```php
function dashboard_admin_blocks() {
  global $theme_key;
  drupal_theme_initialize();
  module_load_include('inc', 'block', 'block.admin');

  // Prepare the blocks for the current theme, and remove those that are
  // currently displayed in non-dashboard regions.
  // @todo This assumes the current page is being displayed using the same
  //   theme that the dashboard is displayed in.
  $blocks = block_admin_display_prepare_blocks($theme_key);
  $dashboard_regions = dashboard_region_descriptions();
  $regions_to_remove = array_diff_key(system_region_list($theme_key, REGIONS_VISIBLE), $dashboard_regions);
  foreach ($blocks as $id => $block) {
    if (isset($regions_to_remove[$block['region']])) {
      unset($blocks[$id]);
    }
  }

  // Pass in the above blocks and dashboard regions to the form, so that only
  // dashboard-related regions will be displayed.
  return drupal_get_form('dashboard_admin_display_form', $blocks, $theme_key, $dashboard_regions);
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
