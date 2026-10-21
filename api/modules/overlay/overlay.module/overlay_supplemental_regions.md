# overlay_supplemental_regions()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 790–792 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L790-L792)
- **Module/theme:** overlay

## Signature

```php
function overlay_supplemental_regions()
```

## Documentation

```text
Returns a list of supplemental page regions for the overlay.

Supplemental overlay regions are those which are technically part of the
parent window, but appear to the user as being related to the overlay
(usually because they are displayed next to, rather than underneath, the
main overlay regions) and therefore need to be dynamically refreshed if any
administrative actions taken within the overlay change their contents.

An example of a typical overlay supplemental region would be the 'page_top'
region, in the case where a toolbar is being displayed there.

@return
  An array of region names that correspond to supplemental overlay regions,
  within the theme that is being used to display the current page.

@see overlay_regions()
```

## Code

```php
function overlay_supplemental_regions() {
  return _overlay_region_list('overlay_supplemental_regions');
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
