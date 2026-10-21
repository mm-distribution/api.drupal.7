# _color_render_images()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 578–650 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L578-L650)
- **Module/theme:** color

## Signature

```php
function _color_render_images($theme, &$info, &$paths, $palette)
```

## Documentation

```text
Renders images that match a given palette.
```

## Code

```php
function _color_render_images($theme, &$info, &$paths, $palette) {
  // Prepare template image.
  $source = $paths['source'] . '/' . $info['base_image'];
  $source = imagecreatefrompng($source);
  $width = imagesx($source);
  $height = imagesy($source);

  // Prepare target buffer.
  $target = imagecreatetruecolor($width, $height);
  imagealphablending($target, TRUE);

  // Fill regions of solid color.
  foreach ($info['fill'] as $color => $fill) {
    imagefilledrectangle($target, $fill[0], $fill[1], $fill[0] + $fill[2], $fill[1] + $fill[3], _color_gd($target, $palette[$color]));
  }

  // Render gradients.
  foreach ($info['gradients'] as $gradient) {
    // Get direction of the gradient.
    if (isset($gradient['direction']) && $gradient['direction'] == 'horizontal') {
      // Horizontal gradient.
      for ($x = 0; $x < $gradient['dimension'][2]; $x++) {
        $color = _color_blend($target, $palette[$gradient['colors'][0]], $palette[$gradient['colors'][1]], $x / ($gradient['dimension'][2] - 1));
        imagefilledrectangle($target, ($gradient['dimension'][0] + $x), $gradient['dimension'][1], ($gradient['dimension'][0] + $x + 1), ($gradient['dimension'][1] + $gradient['dimension'][3]), $color);
      }
    }
    else {
      // Vertical gradient.
      for ($y = 0; $y < $gradient['dimension'][3]; $y++) {
        $color = _color_blend($target, $palette[$gradient['colors'][0]], $palette[$gradient['colors'][1]], $y / ($gradient['dimension'][3] - 1));
        imagefilledrectangle($target, $gradient['dimension'][0], $gradient['dimension'][1] + $y, $gradient['dimension'][0] + $gradient['dimension'][2], $gradient['dimension'][1] + $y + 1, $color);
      }
    }
  }

  // Blend over template.
  imagecopy($target, $source, 0, 0, 0, 0, $width, $height);

  // Clean up template image.
  imagedestroy($source);

  // Cut out slices.
  foreach ($info['slices'] as $file => $coord) {
    list($x, $y, $width, $height) = $coord;
    $base = drupal_basename($file);
    $image = drupal_realpath($paths['target'] . $base);

    // Cut out slice.
    if ($file == 'screenshot.png') {
      $slice = imagecreatetruecolor(150, 90);
      imagecopyresampled($slice, $target, 0, 0, $x, $y, 150, 90, $width, $height);
      variable_set('color_' . $theme . '_screenshot', $image);
    }
    else {
      $slice = imagecreatetruecolor($width, $height);
      imagecopy($slice, $target, 0, 0, $x, $y, $width, $height);
    }

    // Save image.
    imagepng($slice, $image);
    imagedestroy($slice);
    $paths['files'][] = $image;

    // Set standard file permissions for webserver-generated files
    drupal_chmod($image);

    // Build before/after map of image paths.
    $paths['map'][$file] = $base;
  }

  // Clean up target buffer.
  imagedestroy($target);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
