# image_gd_desaturate()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 235–243 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L235-L243)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_desaturate(stdClass $image)
```

## Documentation

```text
Convert an image resource to grayscale.

Note that transparent GIFs loose transparency when desaturated.

@param $image
  An image object. The $image->resource value will be modified by this call.
@return
  TRUE or FALSE, based on success.

@see image_desaturate()
```

## Code

```php
function image_gd_desaturate(stdClass $image) {
  // PHP installations using non-bundled GD do not have imagefilter.
  if (!function_exists('imagefilter')) {
    watchdog('image', 'The image %file could not be desaturated because the imagefilter() function is not available in this PHP installation.', array('%file' => $image->source));
    return FALSE;
  }

  return imagefilter($image->resource, IMG_FILTER_GRAYSCALE);
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
