# image_dimensions_scale()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 203–226 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L203-L226)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_dimensions_scale(array &$dimensions, $width = NULL, $height = NULL, $upscale = FALSE)
```

## Documentation

```text
Scales image dimensions while maintaining aspect ratio.

The resulting dimensions can be smaller for one or both target dimensions.

@param $dimensions
  Dimensions to be modified - an array with components width and height, in
  pixels.
@param $width
  The target width, in pixels. If this value is NULL then the scaling will be
  based only on the height value.
@param $height
  The target height, in pixels. If this value is NULL then the scaling will
  be based only on the width value.
@param $upscale
  Boolean indicating that images smaller than the target dimensions will be
  scaled up. This generally results in a low quality image.

@return
  TRUE if $dimensions was modified, FALSE otherwise.

@see image_scale()
```

## Code

```php
function image_dimensions_scale(array &$dimensions, $width = NULL, $height = NULL, $upscale = FALSE) {
  $aspect = $dimensions['height'] / $dimensions['width'];

  // Calculate one of the dimensions from the other target dimension,
  // ensuring the same aspect ratio as the source dimensions. If one of the
  // target dimensions is missing, that is the one that is calculated. If both
  // are specified then the dimension calculated is the one that would not be
  // calculated to be bigger than its target.
  if (($width && !$height) || ($width && $height && $aspect < $height / $width)) {
    $height = (int) round($width * $aspect);
  }
  else {
    $width = (int) round($height / $aspect);
  }

  // Don't upscale if the option isn't enabled.
  if (!$upscale && ($width >= $dimensions['width'] || $height >= $dimensions['height'])) {
    return FALSE;
  }

  $dimensions['width'] = $width;
  $dimensions['height'] = $height;
  return TRUE;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
