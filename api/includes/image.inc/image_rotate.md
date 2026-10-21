# image_rotate()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 306–308 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L306-L308)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_rotate(stdClass $image, $degrees, $background = NULL)
```

## Documentation

```text
Rotates an image by the given number of degrees.

@param $image
  An image object returned by image_load().
@param $degrees
  The number of (clockwise) degrees to rotate the image.
@param $background
  An hexadecimal integer specifying the background color to use for the
  uncovered area of the image after the rotation. E.g. 0x000000 for black,
  0xff00ff for magenta, and 0xffffff for white. For images that support
  transparency, this will default to transparent. Otherwise it will
  be white.

@return
  TRUE on success, FALSE on failure.

@see image_load()
@see image_gd_rotate()
```

## Code

```php
function image_rotate(stdClass $image, $degrees, $background = NULL) {
  return image_toolkit_invoke('rotate', $image, array($degrees, $background));
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
