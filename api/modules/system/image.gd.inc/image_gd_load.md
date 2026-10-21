# image_gd_load()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 255–276 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L255-L276)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_load(stdClass $image)
```

## Documentation

```text
GD helper function to create an image resource from a file.

@param $image
  An image object. The $image->resource value will populated by this call.
@return
  TRUE or FALSE, based on success.

@see image_load()
```

## Code

```php
function image_gd_load(stdClass $image) {
  $extension = str_replace('jpg', 'jpeg', $image->info['extension']);
  $function = 'imagecreatefrom' . $extension;
  if (function_exists($function) && $image->resource = $function($image->source)) {
    if (imageistruecolor($image->resource)) {
      return TRUE;
    }
    else {
      // Convert indexed images to truecolor, copying the image to a new
      // truecolor resource, so that filters work correctly and don't result
      // in unnecessary dither.
      $resource = image_gd_create_tmp($image, $image->info['width'], $image->info['height']);
      if ($resource) {
        imagecopy($resource, $image->resource, 0, 0, 0, 0, imagesx($resource), imagesy($resource));
        imagedestroy($image->resource);
        $image->resource = $resource;
      }
    }
    return (bool) $image->resource;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
