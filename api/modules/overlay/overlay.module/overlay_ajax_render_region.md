# overlay_ajax_render_region()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 1022–1024 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L1022-L1024)
- **Module/theme:** overlay

## Signature

```php
function overlay_ajax_render_region($region)
```

## Documentation

```text
Prints the markup obtained by rendering a single region of the page.

This function is intended to be called via Ajax.

@param $region
  The name of the page region to render.

@see Drupal.overlay.refreshRegions()
```

## Code

```php
function overlay_ajax_render_region($region) {
  print overlay_render_region($region);
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
