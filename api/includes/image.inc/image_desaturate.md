# image_desaturate()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 354–356 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L354-L356)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_desaturate(stdClass $image)
```

## Documentation

```text
Converts an image to grayscale.

@param $image
  An image object returned by image_load().

@return
  TRUE on success, FALSE on failure.

@see image_load()
@see image_gd_desaturate()
```

## Code

```php
function image_desaturate(stdClass $image) {
  return image_toolkit_invoke('desaturate', $image);
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
