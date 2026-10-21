# image_desaturate_effect()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 226–232 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L226-L232)
- **Module/theme:** image

## Signature

```php
function image_desaturate_effect(&$image, $data)
```

## Documentation

```text
Image effect callback; Desaturate (grayscale) an image resource.

@param $image
  An image object returned by image_load().
@param $data
  An array of attributes to use when performing the desaturate effect.
@return
  TRUE on success. FALSE on failure to desaturate image.
@see image_desaturate()
```

## Code

```php
function image_desaturate_effect(&$image, $data) {
  if (!image_desaturate($image)) {
    watchdog('image', 'Image desaturate failed using the %toolkit toolkit on %path (%mimetype, %dimensions)', array('%toolkit' => $image->toolkit, '%path' => $image->source, '%mimetype' => $image->info['mime_type'], '%dimensions' => $image->info['width'] . 'x' . $image->info['height']), WATCHDOG_ERROR);
    return FALSE;
  }
  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
