# image_gd_save()

- **Type:** Function
- **File:** [`modules/system/image.gd.inc`](_file.md), lines 290–325 · [local source](../../../../source/modules/system/image.gd.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc#L290-L325)
- **Module/theme:** system
- **Topics:** [image](../../../topics/image.md)

## Signature

```php
function image_gd_save(stdClass $image, $destination)
```

## Documentation

```text
GD helper to write an image resource to a destination file.

@param $image
  An image object.
@param $destination
  A string file URI or path where the image should be saved.
@return
  TRUE or FALSE, based on success.

@see image_save()
```

## Code

```php
function image_gd_save(stdClass $image, $destination) {
  $scheme = file_uri_scheme($destination);
  // Work around lack of stream wrapper support in imagejpeg() and imagepng().
  if ($scheme && file_stream_wrapper_valid_scheme($scheme)) {
    // If destination is not local, save image to temporary local file.
    $local_wrappers = file_get_stream_wrappers(STREAM_WRAPPERS_LOCAL);
    if (!isset($local_wrappers[$scheme])) {
      $permanent_destination = $destination;
      $destination = drupal_tempnam('temporary://', 'gd_');
    }
    // Convert stream wrapper URI to normal path.
    $destination = drupal_realpath($destination);
  }

  $extension = str_replace('jpg', 'jpeg', $image->info['extension']);
  $function = 'image' . $extension;
  if (!function_exists($function)) {
    return FALSE;
  }
  if ($extension == 'jpeg') {
    $success = $function($image->resource, $destination, variable_get('image_jpeg_quality', 75));
  }
  else {
    // Always save PNG images with full transparency.
    if ($extension == 'png') {
      imagealphablending($image->resource, FALSE);
      imagesavealpha($image->resource, TRUE);
    }
    $success = $function($image->resource, $destination);
  }
  // Move temporary local file to remote destination.
  if (isset($permanent_destination) && $success) {
    return (bool) file_unmanaged_move($destination, $permanent_destination, FILE_EXISTS_REPLACE);
  }
  return $success;
}
```

---
_Drupal 7.103 · [modules/system/image.gd.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/image.gd.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
