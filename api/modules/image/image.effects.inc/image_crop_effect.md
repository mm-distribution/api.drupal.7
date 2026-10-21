# image_crop_effect()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 177–191 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L177-L191)
- **Module/theme:** image

## Signature

```php
function image_crop_effect(&$image, $data)
```

## Documentation

```text
Image effect callback; Crop an image resource.

@param $image
  An image object returned by image_load().
@param $data
  An array of attributes to use when performing the crop effect with the
  following items:
  - "width": An integer representing the desired width in pixels.
  - "height": An integer representing the desired height in pixels.
  - "anchor": A string describing where the crop should originate in the form
    of "XOFFSET-YOFFSET". XOFFSET is either a number of pixels or
    "left", "center", "right" and YOFFSET is either a number of pixels or
    "top", "center", "bottom".
@return
  TRUE on success. FALSE on failure to crop image.
@see image_crop()
```

## Code

```php
function image_crop_effect(&$image, $data) {
  // Set sane default values.
  $data += array(
    'anchor' => 'center-center',
  );

  list($x, $y) = explode('-', $data['anchor']);
  $x = image_filter_keyword($x, $image->info['width'], $data['width']);
  $y = image_filter_keyword($y, $image->info['height'], $data['height']);
  if (!image_crop($image, $x, $y, $data['width'], $data['height'])) {
    watchdog('image', 'Image crop failed using the %toolkit toolkit on %path (%mimetype, %dimensions)', array('%toolkit' => $image->toolkit, '%path' => $image->source, '%mimetype' => $image->info['mime_type'], '%dimensions' => $image->info['width'] . 'x' . $image->info['height']), WATCHDOG_ERROR);
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
