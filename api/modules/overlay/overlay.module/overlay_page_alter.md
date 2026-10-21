# overlay_page_alter()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 302–320 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L302-L320)
- **Module/theme:** overlay
- **Implements:** [hook_page_alter()](../../system/system.api.php/hook_page_alter.md)

## Signature

```php
function overlay_page_alter(&$page)
```

## Documentation

```text
Implements hook_page_alter().
```

## Code

```php
function overlay_page_alter(&$page) {
  // If we are limiting rendering to a subset of page regions, deny access to
  // all other regions so that they will not be processed.
  if ($regions_to_render = overlay_get_regions_to_render()) {
    $skipped_regions = array_diff(element_children($page), $regions_to_render);
    foreach ($skipped_regions as $skipped_region) {
      $page[$skipped_region]['#access'] = FALSE;
    }
  }

  $mode = overlay_get_mode();
  if ($mode == 'child') {
    // Add the overlay wrapper before the html wrapper.
    array_unshift($page['#theme_wrappers'], 'overlay');
  }
  elseif ($mode == 'parent' && ($message = overlay_disable_message())) {
    $page['page_top']['disable_overlay'] = $message;
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
