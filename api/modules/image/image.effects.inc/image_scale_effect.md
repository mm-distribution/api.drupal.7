# image_scale_effect()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 124–137 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L124-L137)
- **Module/theme:** image

## Signature

```php
function image_scale_effect(&$image, $data)
```

## Documentation

```text
Image effect callback; Scale an image resource.

@param $image
  An image object returned by image_load().
@param $data
  An array of attributes to use when performing the scale effect with the
  following items:
  - "width": An integer representing the desired width in pixels.
  - "height": An integer representing the desired height in pixels.
  - "upscale": A boolean indicating that the image should be upscaled if the
    dimensions are larger than the original image.

@return
  TRUE on success. FALSE on failure to scale image.

@see image_scale()
```

## Code

```php
function image_scale_effect(&$image, $data) {
  // Set sane default values.
  $data += array(
    'width' => NULL,
    'height' => NULL,
    'upscale' => FALSE,
  );

  if (!image_scale($image, $data['width'], $data['height'], $data['upscale'])) {
    watchdog('image', 'Image scale failed using the %toolkit toolkit on %path (%mimetype, %dimensions)', array('%toolkit' => $image->toolkit, '%path' => $image->source, '%mimetype' => $image->info['mime_type'], '%dimensions' => $image->info['width'] . 'x' . $image->info['height']), WATCHDOG_ERROR);
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
