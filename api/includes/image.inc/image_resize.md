# image_resize()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 279–284 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L279-L284)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_resize(stdClass $image, $width, $height)
```

## Documentation

```text
Resizes an image to the given dimensions (ignoring aspect ratio).

@param $image
  An image object returned by image_load().
@param $width
  The target width, in pixels.
@param $height
  The target height, in pixels.

@return
  TRUE on success, FALSE on failure.

@see image_load()
@see image_gd_resize()
```

## Code

```php
function image_resize(stdClass $image, $width, $height) {
  $width = (int) round($width);
  $height = (int) round($height);

  return image_toolkit_invoke('resize', $image, array($width, $height));
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
