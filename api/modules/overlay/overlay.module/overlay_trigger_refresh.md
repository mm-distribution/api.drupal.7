# overlay_trigger_refresh()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 996–1010 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L996-L1010)
- **Module/theme:** overlay

## Signature

```php
function overlay_trigger_refresh()
```

## Documentation

```text
Checks if the parent window needs to be refreshed on this page load.

If the previous page load requested that any page regions be refreshed, or
if it requested that the entire page be refreshed when the overlay closes,
pass that request via JavaScript to the child window, so it can in turn pass
the request to the parent window.

@see overlay_request_refresh()
@see overlay_request_page_refresh()
@see Drupal.overlay.refreshRegions()
```

## Code

```php
function overlay_trigger_refresh() {
  if (!empty($_SESSION['overlay_regions_to_refresh'])) {
    $settings = array(
      'overlayChild' => array(
        'refreshRegions' => $_SESSION['overlay_regions_to_refresh'],
      ),
    );
    drupal_add_js($settings, array('type' => 'setting'));
    unset($_SESSION['overlay_regions_to_refresh']);
  }
  if (!empty($_SESSION['overlay_refresh_parent'])) {
    drupal_add_js(array('overlayChild' => array('refreshPage' => TRUE)), array('type' => 'setting'));
    unset($_SESSION['overlay_refresh_parent']);
  }
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
