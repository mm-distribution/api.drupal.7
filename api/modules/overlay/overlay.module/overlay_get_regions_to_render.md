# overlay_get_regions_to_render()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 831–833 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L831-L833)
- **Module/theme:** overlay

## Signature

```php
function overlay_get_regions_to_render()
```

## Documentation

```text
Returns a list of page regions that rendering should be limited to.

@return
  An array containing the names of the regions that will be rendered when
  drupal_render_page() is called. If empty, then no limits will be imposed,
  and all regions of the page will be rendered.

@see overlay_page_alter()
@see overlay_block_list_alter()
@see overlay_set_regions_to_render()
```

## Code

```php
function overlay_get_regions_to_render() {
  return overlay_set_regions_to_render();
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
