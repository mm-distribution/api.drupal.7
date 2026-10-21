# image_scale_dimensions()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 153–157 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L153-L157)
- **Module/theme:** image

## Signature

```php
function image_scale_dimensions(array &$dimensions, array $data)
```

## Documentation

```text
Image dimensions callback; Scale.

@param $dimensions
  Dimensions to be modified - an array with components width and height, in
  pixels.
@param $data
  An array of attributes to use when performing the scale effect with the
  following items:
  - "width": An integer representing the desired width in pixels.
  - "height": An integer representing the desired height in pixels.
  - "upscale": A boolean indicating that the image should be upscaled if the
    dimensions are larger than the original image.
```

## Code

```php
function image_scale_dimensions(array &$dimensions, array $data) {
  if ($dimensions['width'] && $dimensions['height']) {
    image_dimensions_scale($dimensions, $data['width'], $data['height'], $data['upscale']);
  }
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
