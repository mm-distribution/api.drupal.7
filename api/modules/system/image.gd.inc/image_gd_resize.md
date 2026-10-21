# image_gd_resize()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 78–91 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L78-L91)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_resize(stdClass $image, $width, $height)
```

## Documentation

```text
Scale an image to the specified size using GD.

@param $image
  An image object. The $image->resource, $image->info['width'], and
  $image->info['height'] values will be modified by this call.
@param $width
  The new width of the resized image, in pixels.
@param $height
  The new height of the resized image, in pixels.
@return
  TRUE or FALSE, based on success.

@see image_resize()
```

## Code

```php
function image_gd_resize(stdClass $image, $width, $height) {
  $res = image_gd_create_tmp($image, $width, $height);

  if (!imagecopyresampled($res, $image->resource, 0, 0, 0, 0, $width, $height, $image->info['width'], $image->info['height'])) {
    return FALSE;
  }

  imagedestroy($image->resource);
  // Update image object.
  $image->resource = $res;
  $image->info['width'] = $width;
  $image->info['height'] = $height;
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
