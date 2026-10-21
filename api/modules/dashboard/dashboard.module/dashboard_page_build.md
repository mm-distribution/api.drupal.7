# dashboard_page_build()

- **Type:** Function
- **File:** [`modules/dashboard/dashboard.module`](_file.md), lines 139–200 · [local source](../../../../source/modules/dashboard/dashboard.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module#L139-L200)
- **Module/theme:** dashboard
- **Implements:** [hook_page_build()](../../system/system.api.php/hook_page_build.md)

## Signature

```php
function dashboard_page_build(&$page)
```

## Documentation

```text
Implements hook_page_build().

Display dashboard blocks in the main content region.
```

## Code

```php
function dashboard_page_build(&$page) {
  global $theme_key;

  if (dashboard_is_visible()) {
    $block_info = array();

    // Create a wrapper for the dashboard itself, then insert each dashboard
    // region into it.
    $page['content']['dashboard'] = array('#theme_wrappers' => array('dashboard'));
    foreach (dashboard_regions() as $region) {
      // Do not show dashboard blocks that are disabled.
      if ($region == 'dashboard_inactive') {
        continue;
      }
      // Insert regions even when they are empty, so that they will be
      // displayed when the dashboard is being configured.
      $page['content']['dashboard'][$region] = !empty($page[$region]) ? $page[$region] : array();
      $page['content']['dashboard'][$region]['#dashboard_region'] = $region;
      // Allow each dashboard region to be themed differently, or fall back on
      // the generic theme wrapper function for dashboard regions.
      $page['content']['dashboard'][$region]['#theme_wrappers'][] = array($region, 'dashboard_region');
      unset($page[$region]);
      $blocks_found = array();
      foreach ($page['content']['dashboard'][$region] as $item) {
        if (isset($item['#theme_wrappers']) && is_array($item['#theme_wrappers']) && in_array('block', $item['#theme_wrappers'])) {
          // If this item is a block, ensure it has a subject.
          if (empty($item['#block']->subject)) {
            // Locally cache info data for the object for all blocks, in case
            // we find a block similarly missing title from the same module.
            if (!isset($block_info[$item['#block']->module])) {
              $block_info[$item['#block']->module] = module_invoke($item['#block']->module, 'block_info');
            }
            $item['#block']->subject = $block_info[$item['#block']->module][$item['#block']->delta]['info'];
          }
          $blocks_found[$item['#block']->module . '_' . $item['#block']->delta] = TRUE;
        }
      }

      // Find blocks which were not yet displayed on the page (were empty), and
      // add placeholder items in their place for rendering.
      $block_list = db_select('block')
        ->condition('theme', $theme_key)
        ->condition('status', 1)
        ->condition('region', $region)
        ->fields('block')
        ->execute();
      foreach ($block_list as $block) {
        if (!isset($blocks_found[$block->module . '_' . $block->delta])) {
          $block->enabled = $block->page_match = TRUE;
          $block->content = array('#markup' => '<div class="dashboard-block-empty">(empty)</div>');
          if (!isset($block_info[$block->module])) {
            $block_info[$block->module] = module_invoke($block->module, 'block_info');
          }
          $block->subject = t('@title', array('@title' => $block_info[$block->module][$block->delta]['info']));
          $block_render = array($block->module . '_' . $block->delta => $block);
          $build = _block_get_renderable_array($block_render);
          $page['content']['dashboard'][$block->region][] = $build;
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/dashboard/dashboard.module](https://github.com/drupal/drupal/blob/7.103/modules/dashboard/dashboard.module) · Licensed GPL-2.0-or-later (see LICENSE)._
