# file_validate_image_resolution()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1895–1929 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1895-L1929)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_validate_image_resolution(stdClass $file, $maximum_dimensions = 0, $minimum_dimensions = 0)
```

## Documentation

```text
Verifies that image dimensions are within the specified maximum and minimum.

Non-image files will be ignored. If an image toolkit is available the image
will be scaled to fit within the desired maximum dimensions.

@param $file
  A Drupal file object. This function may resize the file affecting its
  size.
@param $maximum_dimensions
  An optional string in the form WIDTHxHEIGHT e.g. '640x480' or '85x85'. If
  an image toolkit is installed the image will be resized down to these
  dimensions. A value of 0 indicates no restriction on size, so resizing
  will be attempted.
@param $minimum_dimensions
  An optional string in the form WIDTHxHEIGHT. This will check that the
  image meets a minimum size. A value of 0 indicates no restriction.

@return
  An array. If the file is an image and did not meet the requirements, it
  will contain an error message.

@see hook_file_validate()
```

## Code

```php
function file_validate_image_resolution(stdClass $file, $maximum_dimensions = 0, $minimum_dimensions = 0) {
  $errors = array();

  // Check first that the file is an image.
  if ($info = image_get_info($file->uri)) {
    if ($maximum_dimensions) {
      // Check that it is smaller than the given dimensions.
      list($width, $height) = explode('x', $maximum_dimensions);
      if ($info['width'] > $width || $info['height'] > $height) {
        // Try to resize the image to fit the dimensions.
        if ($image = image_load($file->uri)) {
          image_scale($image, $width, $height);
          image_save($image);
          // Update the image info since we have resized it.
          $info = $image->info;
          $file->filesize = $image->info['file_size'];
          drupal_set_message(t('The image was resized to fit within the maximum allowed dimensions of %dimensions pixels.', array('%dimensions' => $maximum_dimensions)));
        }
        else {
          $errors[] = t('The image is too large; the maximum dimensions are %dimensions pixels.', array('%dimensions' => $maximum_dimensions));
        }
      }
    }

    if ($minimum_dimensions) {
      // Check that it is larger than the given dimensions.
      list($width, $height) = explode('x', $minimum_dimensions);
      if ($info['width'] < $width || $info['height'] < $height) {
        $errors[] = t('The image is too small; the minimum dimensions are %dimensions pixels.', array('%dimensions' => $minimum_dimensions));
      }
    }
  }

  return $errors;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
