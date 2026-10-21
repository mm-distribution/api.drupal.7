# overlay_set_regions_to_render()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 853–859 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L853-L859)
- **Module/theme:** overlay

## Signature

```php
function overlay_set_regions_to_render($regions = NULL)
```

## Documentation

```text
Sets the regions of the page that rendering will be limited to.

@param $regions
  (Optional) An array containing the names of the regions that should be
  rendered when drupal_render_page() is called. Pass in an empty array to
  remove all limits and cause drupal_render_page() to render all page
  regions (the default behavior). If this parameter is omitted, no change
  will be made to the current list of regions to render.

@return
  The current list of regions to render, or an empty array if the regions
  are not being limited.

@see overlay_page_alter()
@see overlay_block_list_alter()
@see overlay_get_regions_to_render()
```

## Code

```php
function overlay_set_regions_to_render($regions = NULL) {
  $regions_to_render = &drupal_static(__FUNCTION__, array());
  if (isset($regions)) {
    $regions_to_render = $regions;
  }
  return $regions_to_render;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
