# image_gd_rotate()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 112–185 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L112-L185)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_rotate(stdClass $image, $degrees, $background = NULL)
```

## Documentation

```text
Rotate an image the given number of degrees.

@param $image
  An image object. The $image->resource, $image->info['width'], and
  $image->info['height'] values will be modified by this call.
@param $degrees
  The number of (clockwise) degrees to rotate the image.
@param $background
  An hexadecimal integer specifying the background color to use for the
  uncovered area of the image after the rotation. E.g. 0x000000 for black,
  0xff00ff for magenta, and 0xffffff for white. For images that support
  transparency, this will default to transparent. Otherwise it will
  be white.
@return
  TRUE or FALSE, based on success.

@see image_rotate()
```

## Code

```php
function image_gd_rotate(stdClass $image, $degrees, $background = NULL) {
  // PHP installations using non-bundled GD do not have imagerotate.
  if (!function_exists('imagerotate')) {
    watchdog('image', 'The image %file could not be rotated because the imagerotate() function is not available in this PHP installation.', array('%file' => $image->source));
    return FALSE;
  }

  // PHP 5.5 GD bug: https://bugs.php.net/bug.php?id=65148: To prevent buggy
  // behavior on negative multiples of 90 degrees we convert any negative
  // angle to a positive one between 0 and 360 degrees.
  $degrees -= floor($degrees / 360) * 360;

  // Convert the hexadecimal background value to a RGBA array.
  if (isset($background)) {
    $background = array(
      'red' => $background >> 16 & 0xFF,
      'green' => $background >> 8 & 0xFF,
      'blue' => $background & 0xFF,
      'alpha' => 0,
    );
  }
  else {
    // Background color is not specified: use transparent white as background.
    $background = array(
      'red' => 255,
      'green' => 255,
      'blue' => 255,
      'alpha' => 127
    );
  }

  // Store the color index for the background as that is what GD uses.
  $background_idx = imagecolorallocatealpha($image->resource, $background['red'], $background['green'], $background['blue'], $background['alpha']);

  // Images are assigned a new color palette when rotating, removing any
  // transparency flags. For GIF images, keep a record of the transparent color.
  if ($image->info['extension'] == 'gif') {
    // GIF does not work with a transparency channel, but can define 1 color
    // in its palette to act as transparent.

    // Get the current transparent color, if any.
    $gif_transparent_id = imagecolortransparent($image->resource);
    if ($gif_transparent_id !== -1) {
      // The gif already has a transparent color set: remember it to set it on
      // the rotated image as well.
      $transparent_gif_color = imagecolorsforindex($image->resource, $gif_transparent_id);

      if ($background['alpha'] >= 127) {
        // We want a transparent background: use the color already set to act
        // as transparent, as background.
        $background_idx = $gif_transparent_id;
      }
    }
    else {
      // The gif does not currently have a transparent color set.
      if ($background['alpha'] >= 127) {
        // But as the background is transparent, it should get one.
        $transparent_gif_color = $background;
      }
    }
  }

  $image->resource = imagerotate($image->resource, 360 - $degrees, $background_idx);

  // GIFs need to reassign the transparent color after performing the rotate.
  if (isset($transparent_gif_color)) {
    $background = imagecolorexactalpha($image->resource, $transparent_gif_color['red'], $transparent_gif_color['green'], $transparent_gif_color['blue'], $transparent_gif_color['alpha']);
    imagecolortransparent($image->resource, $background);
  }

  $image->info['width'] = imagesx($image->resource);
  $image->info['height'] = imagesy($image->resource);
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
