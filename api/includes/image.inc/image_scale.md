# image_scale()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 252–261 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L252-L261)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_scale(stdClass $image, $width = NULL, $height = NULL, $upscale = FALSE)
```

## Documentation

```text
Scales an image while maintaining aspect ratio.

The resulting image can be smaller for one or both target dimensions.

@param $image
  An image object returned by image_load().
@param $width
  The target width, in pixels. If this value is NULL then the scaling will
  be based only on the height value.
@param $height
  The target height, in pixels. If this value is NULL then the scaling will
  be based only on the width value.
@param $upscale
  Boolean indicating that files smaller than the dimensions will be scaled
  up. This generally results in a low quality image.

@return
  TRUE on success, FALSE on failure.

@see image_dimensions_scale()
@see image_load()
@see image_scale_and_crop()
```

## Code

```php
function image_scale(stdClass $image, $width = NULL, $height = NULL, $upscale = FALSE) {
  $dimensions = $image->info;

  // Scale the dimensions - if they don't change then just return success.
  if (!image_dimensions_scale($dimensions, $width, $height, $upscale)) {
    return TRUE;
  }

  return image_resize($image, $dimensions['width'], $dimensions['height']);
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
