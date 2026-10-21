# overlay_request_refresh()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 970–973 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L970-L973)
- **Module/theme:** overlay

## Signature

```php
function overlay_request_refresh($region)
```

## Documentation

```text
Requests that the parent window refreshes a particular page region.

@param $region
  The name of the page region to refresh. The parent window will trigger a
  refresh of this region on the next page load.

@see overlay_trigger_refresh()
@see Drupal.overlay.refreshRegions()
```

## Code

```php
function overlay_request_refresh($region) {
  $class = drupal_region_class($region);
  $_SESSION['overlay_regions_to_refresh'][] = array($class => $region);
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
