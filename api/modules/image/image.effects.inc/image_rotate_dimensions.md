# image_rotate_dimensions()

- **Type:** Function
- **File:** [`modules/image/image.effects.inc`](_file.md), lines 301–314 · [local source](../../../../source/modules/image/image.effects.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc#L301-L314)
- **Module/theme:** image

## Signature

```php
function image_rotate_dimensions(array &$dimensions, array $data)
```

## Documentation

```text
Image dimensions callback; Rotate.

@param $dimensions
  Dimensions to be modified - an array with components width and height, in
  pixels.
@param $data
  An array of attributes to use when performing the rotate effect containing
  the following items:
  - "degrees": The number of (clockwise) degrees to rotate the image.
  - "random": A boolean indicating that a random rotation angle should be
    used for this image. The angle specified in "degrees" is used as a
    positive and negative maximum.
```

## Code

```php
function image_rotate_dimensions(array &$dimensions, array $data) {
  // If the rotate is not random and the angle is a multiple of 90 degrees,
  // then the new dimensions can be determined.
  if (!$data['random'] && ((int) ($data['degrees']) == $data['degrees']) && ($data['degrees'] % 90 == 0)) {
    if ($data['degrees'] % 180 != 0) {
      $temp = $dimensions['width'];
      $dimensions['width'] = $dimensions['height'];
      $dimensions['height'] = $temp;
    }
  }
  else {
    $dimensions['width'] = $dimensions['height'] = NULL;
  }
}
```

---
_Drupal 7.103 · [modules/image/image.effects.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.effects.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
