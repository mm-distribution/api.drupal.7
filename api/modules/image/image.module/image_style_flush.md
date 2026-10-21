# image_style_flush()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1058–1085 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1058-L1085)
- **Module/theme:** image

## Signature

```php
function image_style_flush($style)
```

## Documentation

```text
Flushes cached media for a style.

@param $style
  An image style array.
```

## Code

```php
function image_style_flush($style) {
  // Delete the style directory in each registered wrapper.
  $wrappers = file_get_stream_wrappers(STREAM_WRAPPERS_WRITE_VISIBLE);
  foreach ($wrappers as $wrapper => $wrapper_data) {
    if (file_exists($directory = $wrapper . '://styles/' . $style['name'])) {
      file_unmanaged_delete_recursive($directory);
    }
  }

  // Let other modules update as necessary on flush.
  module_invoke_all('image_style_flush', $style);

  // Clear image style and effect caches.
  cache_clear_all('image_styles', 'cache');
  cache_clear_all('image_effects:', 'cache', TRUE);
  drupal_static_reset('image_styles');
  drupal_static_reset('image_effects');

  // Clear field caches so that formatters may be added for this style.
  field_info_cache_clear();
  drupal_theme_rebuild();

  // Clear page caches when flushing.
  if (module_exists('block')) {
    cache_clear_all('*', 'cache_block', TRUE);
  }
  cache_clear_all('*', 'cache_page', TRUE);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
