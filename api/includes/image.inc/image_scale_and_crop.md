# image_scale_and_crop()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 169–178 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L169-L178)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_scale_and_crop(stdClass $image, $width, $height)
```

## Documentation

```text
Scales an image to the exact width and height given.

This function achieves the target aspect ratio by cropping the original image
equally on both sides, or equally on the top and bottom. This function is
useful to create uniform sized avatars from larger images.

The resulting image always has the exact target dimensions.

@param $image
  An image object returned by image_load().
@param $width
  The target width, in pixels.
@param $height
  The target height, in pixels.

@return
  TRUE on success, FALSE on failure.

@see image_load()
@see image_resize()
@see image_crop()
```

## Code

```php
function image_scale_and_crop(stdClass $image, $width, $height) {
  $scale = max($width / $image->info['width'], $height / $image->info['height']);
  $x = ($image->info['width'] * $scale - $width) / 2;
  $y = ($image->info['height'] * $scale - $height) / 2;

  if (image_resize($image, $image->info['width'] * $scale, $image->info['height'] * $scale)) {
    return image_crop($image, $x, $y, $width, $height);
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
