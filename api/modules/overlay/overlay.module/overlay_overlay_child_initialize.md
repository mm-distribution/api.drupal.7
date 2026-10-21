# overlay_overlay_child_initialize()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 699–722 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L699-L722)
- **Module/theme:** overlay
- **Implements:** [hook_overlay_child_initialize()](../overlay.api.php/hook_overlay_child_initialize.md)

## Signature

```php
function overlay_overlay_child_initialize()
```

## Documentation

```text
Implements hook_overlay_child_initialize().
```

## Code

```php
function overlay_overlay_child_initialize() {
  // Check if the parent window needs to refresh any page regions on this page
  // request.
  overlay_trigger_refresh();
  // If this is a POST request, or a GET request with a token parameter, we
  // have an indication that something in the supplemental regions of the
  // overlay might change during the current page request. We therefore store
  // the initial rendered content of those regions here, so that we can compare
  // it to the same content rendered in overlay_exit(), at the end of the page
  // request. This allows us to check if anything actually did change, and, if
  // so, trigger an immediate Ajax refresh of the parent window.
  if (!empty($_POST) || isset($_GET['token'])) {
    foreach (overlay_supplemental_regions() as $region) {
      overlay_store_rendered_content($region, overlay_render_region($region));
    }
    // In addition, notify the parent window that when the overlay closes,
    // the entire parent window should be refreshed.
    overlay_request_page_refresh();
  }
  // Indicate that when the main page rendering occurs later in the page
  // request, only the regions that appear within the overlay should be
  // rendered.
  overlay_set_regions_to_render(overlay_regions());
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
