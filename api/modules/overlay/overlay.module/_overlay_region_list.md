# _overlay_region_list()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 808–817 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L808-L817)
- **Module/theme:** overlay

## Signature

```php
function _overlay_region_list($type)
```

## Documentation

```text
Returns a list of page regions related to the overlay.

@param $type
  The type of regions to return. This can either be 'overlay_regions' or
  'overlay_supplemental_regions'.

@return
  An array of region names of the given type, within the theme that is being
  used to display the current page.

@see overlay_regions()
@see overlay_supplemental_regions()
```

## Code

```php
function _overlay_region_list($type) {
  // Obtain the current theme. We need to first make sure the theme system is
  // initialized, since this function can be called early in the page request.
  drupal_theme_initialize();
  $themes = list_themes();
  $theme = $themes[$GLOBALS['theme']];
  // Return the list of regions stored within the theme's info array, or an
  // empty array if no regions of the appropriate type are defined.
  return !empty($theme->info[$type]) ? $theme->info[$type] : array();
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
