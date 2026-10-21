# image_gd_crop()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 206–221 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L206-L221)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_crop(stdClass $image, $x, $y, $width, $height)
```

## Documentation

```text
Crop an image using the GD toolkit.

@param $image
  An image object. The $image->resource, $image->info['width'], and
  $image->info['height'] values will be modified by this call.
@param $x
  The starting x offset at which to start the crop, in pixels.
@param $y
  The starting y offset at which to start the crop, in pixels.
@param $width
  The width of the cropped area, in pixels.
@param $height
  The height of the cropped area, in pixels.
@return
  TRUE or FALSE, based on success.

@see image_crop()
```

## Code

```php
function image_gd_crop(stdClass $image, $x, $y, $width, $height) {
  $width = (int) $width;
  $height = (int) $height;
  $res = image_gd_create_tmp($image, $width, $height);

  if (!imagecopyresampled($res, $image->resource, 0, 0, (int) $x, (int) $y, $width, $height, $width, $height)) {
    return FALSE;
  }

  // Destroy the original image and return the modified image.
  imagedestroy($image->resource);
  $image->resource = $res;
  $image->info['width'] = $width;
  $image->info['height'] = $height;
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
