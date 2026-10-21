# image_crop()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 331–340 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L331-L340)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_crop(stdClass $image, $x, $y, $width, $height)
```

## Documentation

```text
Crops an image to a rectangle specified by the given dimensions.

@param $image
  An image object returned by image_load().
@param $x
  The top left coordinate, in pixels, of the crop area (x axis value).
@param $y
  The top left coordinate, in pixels, of the crop area (y axis value).
@param $width
  The target width, in pixels.
@param $height
  The target height, in pixels.

@return
  TRUE on success, FALSE on failure.

@see image_load()
@see image_scale_and_crop()
@see image_gd_crop()
```

## Code

```php
function image_crop(stdClass $image, $x, $y, $width, $height) {
  $aspect = $image->info['height'] / $image->info['width'];
  if (empty($height)) $height = $width / $aspect;
  if (empty($width)) $width = $height * $aspect;

  $width = (int) round($width);
  $height = (int) round($height);

  return image_toolkit_invoke('crop', $image, array($x, $y, $width, $height));
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
