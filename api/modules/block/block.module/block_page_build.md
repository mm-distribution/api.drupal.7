# block_page_build()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 256–305 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L256-L305)
- **Module/theme:** block
- **Implements:** [hook_page_build()](../../system/system.api.php/hook_page_build.md)

## Signature

```php
function block_page_build(&$page)
```

## Documentation

```text
Implements hook_page_build().

Renders blocks into their regions.
```

## Code

```php
function block_page_build(&$page) {
  global $theme;

  // The theme system might not yet be initialized. We need $theme.
  drupal_theme_initialize();

  // Fetch a list of regions for the current theme.
  $all_regions = system_region_list($theme);

  $item = menu_get_item();
  if ($item === FALSE || $item['path'] != 'admin/structure/block/demo/' . $theme) {
    // Load all region content assigned via blocks.
    foreach (array_keys($all_regions) as $region) {
      // Assign blocks to region.
      if ($blocks = block_get_blocks_by_region($region)) {
        $page[$region] = $blocks;
      }
    }
    // Once we've finished attaching all blocks to the page, clear the static
    // cache to allow modules to alter the block list differently in different
    // contexts. For example, any code that triggers hook_page_build() more
    // than once in the same page request may need to alter the block list
    // differently each time, so that only certain parts of the page are
    // actually built. We do not clear the cache any earlier than this, though,
    // because it is used each time block_get_blocks_by_region() gets called
    // above.
    drupal_static_reset('block_list');
  }
  else {
    // Append region description if we are rendering the regions demo page.
    if ($item['path'] == 'admin/structure/block/demo/' . $theme) {
      foreach (system_region_list($theme, REGIONS_VISIBLE, FALSE) as $region) {
        $description = '<div class="block-region">' . $all_regions[$region] . '</div>';
        $page[$region]['block_description'] = array(
          '#markup' => $description,
          '#weight' => 15,
        );
      }
      $page['page_top']['backlink'] = array(
        '#type' => 'link',
        '#title' => t('Exit block region demonstration'),
        '#href' => 'admin/structure/block' . (variable_get('theme_default', 'bartik') == $theme ? '' : '/list/' . $theme),
        // Add the "overlay-restore" class to indicate this link should restore
        // the context in which the region demonstration page was opened.
        '#options' => array('attributes' => array('class' => array('block-demo-backlink', 'overlay-restore'))),
        '#weight' => -10,
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
