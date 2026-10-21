# image_scale_and_crop_effect()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 207–213 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L207-L213)
- **Module/theme:** image

## Signature

```php
function image_scale_and_crop_effect(&$image, $data)
```

## Documentation

```text
Image effect callback; Scale and crop an image resource.

@param $image
  An image object returned by image_load().
@param $data
  An array of attributes to use when performing the scale and crop effect
  with the following items:
  - "width": An integer representing the desired width in pixels.
  - "height": An integer representing the desired height in pixels.
@return
  TRUE on success. FALSE on failure to scale and crop image.
@see image_scale_and_crop()
```

## Code

```php
function image_scale_and_crop_effect(&$image, $data) {
  if (!image_scale_and_crop($image, $data['width'], $data['height'])) {
    watchdog('image', 'Image scale and crop failed using the %toolkit toolkit on %path (%mimetype, %dimensions)', array('%toolkit' => $image->toolkit, '%path' => $image->source, '%mimetype' => $image->info['mime_type'], '%dimensions' => $image->info['width'] . 'x' . $image->info['height']), WATCHDOG_ERROR);
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
