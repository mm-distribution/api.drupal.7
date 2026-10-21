# image_gd_create_tmp()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 339–382 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L339-L382)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_create_tmp(stdClass $image, $width, $height)
```

## Documentation

```text
Create a truecolor image preserving transparency from a provided image.

@param $image
  An image object.
@param $width
  The new width of the new image, in pixels.
@param $height
  The new height of the new image, in pixels.
@return
  A GD image handle.
```

## Code

```php
function image_gd_create_tmp(stdClass $image, $width, $height) {
  $res = imagecreatetruecolor($width, $height);

  if ($image->info['extension'] == 'gif') {
    // Find out if a transparent color is set, will return -1 if no
    // transparent color has been defined in the image.
    $transparent = imagecolortransparent($image->resource);

    if ($transparent >= 0) {
      // Find out the number of colors in the image palette. It will be 0 for
      // truecolor images.
      $palette_size = imagecolorstotal($image->resource);
      if ($palette_size == 0 || $transparent < $palette_size) {
        // Set the transparent color in the new resource, either if it is a
        // truecolor image or if the transparent color is part of the palette.
        // Since the index of the transparency color is a property of the
        // image rather than of the palette, it is possible that an image
        // could be created with this index set outside the palette size (see
        // http://stackoverflow.com/a/3898007).
        $transparent_color = imagecolorsforindex($image->resource, $transparent);
        $transparent = imagecolorallocate($res, $transparent_color['red'], $transparent_color['green'], $transparent_color['blue']);

        // Flood with our new transparent color.
        imagefill($res, 0, 0, $transparent);
        imagecolortransparent($res, $transparent);
      }
      else {
        imagefill($res, 0, 0, imagecolorallocate($res, 255, 255, 255));
      }
    }
  }
  elseif ($image->info['extension'] == 'png') {
    imagealphablending($res, FALSE);
    $transparency = imagecolorallocatealpha($res, 0, 0, 0, 127);
    imagefill($res, 0, 0, $transparency);
    imagealphablending($res, TRUE);
    imagesavealpha($res, TRUE);
  }
  else {
    imagefill($res, 0, 0, imagecolorallocate($res, 255, 255, 255));
  }

  return $res;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
