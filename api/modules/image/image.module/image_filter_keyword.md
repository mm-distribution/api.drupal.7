# image_filter_keyword()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1471–1485 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1471-L1485)
- **Module/theme:** image

## Signature

```php
function image_filter_keyword($value, $current_pixels, $new_pixels)
```

## Documentation

```text
Accepts a keyword (center, top, left, etc) and returns it as a pixel offset.

@param $value
@param $current_pixels
@param $new_pixels
```

## Code

```php
function image_filter_keyword($value, $current_pixels, $new_pixels) {
  switch ($value) {
    case 'top':
    case 'left':
      return 0;

    case 'bottom':
    case 'right':
      return $current_pixels - $new_pixels;

    case 'center':
      return $current_pixels / 2 - $new_pixels / 2;
  }
  return $value;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
