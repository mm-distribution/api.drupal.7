# overlay_exit()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 190–212 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L190-L212)
- **Module/theme:** overlay
- **Implements:** [hook_exit()](../../system/system.api.php/hook_exit.md)

## Signature

```php
function overlay_exit()
```

## Documentation

```text
Implements hook_exit().

When viewing an overlay child page, check if we need to trigger a refresh of
the supplemental regions of the overlay on the next page request.
```

## Code

```php
function overlay_exit() {
  // Check that we are in an overlay child page. Note that this should never
  // return TRUE on a cached page view, since the child mode is not set until
  // overlay_init() is called.
  if (overlay_get_mode() == 'child') {
    // Load any markup that was stored earlier in the page request, via calls
    // to overlay_store_rendered_content(). If none was stored, this is not a
    // page request where we expect any changes to the overlay supplemental
    // regions to have occurred, so we do not need to proceed any further.
    $original_markup = overlay_get_rendered_content();
    if (!empty($original_markup)) {
      // Compare the original markup to the current markup that we get from
      // rendering each overlay supplemental region now. If they don't match,
      // something must have changed, so we request a refresh of that region
      // within the parent window on the next page request.
      foreach (overlay_supplemental_regions() as $region) {
        if (!isset($original_markup[$region]) || $original_markup[$region] != overlay_render_region($region)) {
          overlay_request_refresh($region);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
