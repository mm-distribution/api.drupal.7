# image_resize_effect()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 80–86 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L80-L86)
- **Module/theme:** image

## Signature

```php
function image_resize_effect(&$image, $data)
```

## Documentation

```text
Image effect callback; Resize an image resource.

@param $image
  An image object returned by image_load().
@param $data
  An array of attributes to use when performing the resize effect with the
  following items:
  - "width": An integer representing the desired width in pixels.
  - "height": An integer representing the desired height in pixels.

@return
  TRUE on success. FALSE on failure to resize image.

@see image_resize()
```

## Code

```php
function image_resize_effect(&$image, $data) {
  if (!image_resize($image, $data['width'], $data['height'])) {
    watchdog('image', 'Image resize failed using the %toolkit toolkit on %path (%mimetype, %dimensions)', array('%toolkit' => $image->toolkit, '%path' => $image->source, '%mimetype' => $image->info['mime_type'], '%dimensions' => $image->info['width'] . 'x' . $image->info['height']), WATCHDOG_ERROR);
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
