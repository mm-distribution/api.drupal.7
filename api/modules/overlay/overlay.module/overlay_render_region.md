# overlay_render_region()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 878–916 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L878-L916)
- **Module/theme:** overlay

## Signature

```php
function overlay_render_region($region)
```

## Documentation

```text
Renders an individual page region.

This function is primarily intended to be used for checking the content of
supplemental overlay regions (e.g., a region containing a toolbar). Passing
in a region that is intended to display the main page content is not
supported; the region will be rendered by this function, but the main page
content will not appear in it. In addition, although this function returns
the rendered HTML for the provided region, it does not place it on the final
page, nor add any of its associated JavaScript or CSS to the page.

@param $region
  The name of the page region that should be rendered.

@return
  The rendered HTML of the provided region.
```

## Code

```php
function overlay_render_region($region) {
  // Indicate the region that we will be rendering, so that other regions will
  // be hidden by overlay_page_alter() and overlay_block_list_alter().
  overlay_set_regions_to_render(array($region));
  // Do what is necessary to force drupal_render_page() to only display HTML
  // from the requested region. Specifically, declare that the main page
  // content does not need to automatically be added to the page, and pass in
  // a page array that has all theme functions removed (so that overall HTML
  // for the page will not be added either).
  $system_main_content_added = &drupal_static('system_main_content_added');
  $system_main_content_added = TRUE;
  $page = array(
    '#type' => 'page',
    '#theme' => NULL,
    '#theme_wrappers' => array(),
  );
  // Render the region, but do not cache any JavaScript or CSS associated with
  // it. This region might not be included the next time drupal_render_page()
  // is called, and we do not want its JavaScript or CSS to erroneously appear
  // on the final rendered page.
  $original_js = drupal_add_js();
  $original_css = drupal_add_css();
  $original_libraries = drupal_static('drupal_add_library');
  $js = &drupal_static('drupal_add_js');
  $css = &drupal_static('drupal_add_css');
  $libraries = &drupal_static('drupal_add_library');
  $markup = drupal_render_page($page);
  $js = $original_js;
  $css = $original_css;
  $libraries = $original_libraries;
  // Indicate that the main page content has not, in fact, been displayed, so
  // that future calls to drupal_render_page() will be able to render it
  // correctly.
  $system_main_content_added = FALSE;
  // Restore the original behavior of rendering all regions for the next time
  // drupal_render_page() is called.
  overlay_set_regions_to_render(array());
  return $markup;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
