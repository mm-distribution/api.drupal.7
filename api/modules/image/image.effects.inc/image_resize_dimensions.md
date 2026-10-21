# image_resize_dimensions()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 100–104 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L100-L104)
- **Module/theme:** image

## Signature

```php
function image_resize_dimensions(array &$dimensions, array $data)
```

## Documentation

```text
Image dimensions callback; Resize.

@param $dimensions
  Dimensions to be modified - an array with components width and height, in
  pixels.
@param $data
  An array of attributes to use when performing the resize effect with the
  following items:
  - "width": An integer representing the desired width in pixels.
  - "height": An integer representing the desired height in pixels.
```

## Code

```php
function image_resize_dimensions(array &$dimensions, array $data) {
  // The new image will have the exact dimensions defined for the effect.
  $dimensions['width'] = $data['width'];
  $dimensions['height'] = $data['height'];
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
