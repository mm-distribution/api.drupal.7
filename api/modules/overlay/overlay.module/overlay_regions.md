# overlay_regions()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 768–770 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L768-L770)
- **Module/theme:** overlay

## Signature

```php
function overlay_regions()
```

## Documentation

```text
Returns a list of page regions that appear in the overlay.

Overlay regions correspond to the entire contents of the overlay child
window and are refreshed each time a new page request is made within the
overlay.

@return
  An array of region names that correspond to those which appear in the
  overlay, within the theme that is being used to display the current page.

@see overlay_supplemental_regions()
```

## Code

```php
function overlay_regions() {
  return _overlay_region_list('overlay_regions');
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
