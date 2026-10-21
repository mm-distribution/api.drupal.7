# image_style_create_derivative()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 990–1017 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L990-L1017)
- **Module/theme:** image

## Signature

```php
function image_style_create_derivative($style, $source, $destination)
```

## Documentation

```text
Creates a new image derivative based on an image style.

Generates an image derivative by creating the destination folder (if it does
not already exist), applying all image effects defined in $style['effects'],
and saving a cached version of the resulting image.

@param $style
  An image style array.
@param $source
  Path of the source file.
@param $destination
  Path or URI of the destination file.

@return
  TRUE if an image derivative was generated, or FALSE if the image derivative
  could not be generated.

@see image_style_load()
```

## Code

```php
function image_style_create_derivative($style, $source, $destination) {
  // If the source file doesn't exist, return FALSE without creating folders.
  if (!$image = image_load($source)) {
    return FALSE;
  }

  // Get the folder for the final location of this style.
  $directory = drupal_dirname($destination);

  // Build the destination folder tree if it doesn't already exist.
  if (!file_prepare_directory($directory, FILE_CREATE_DIRECTORY | FILE_MODIFY_PERMISSIONS)) {
    watchdog('image', 'Failed to create style directory: %directory', array('%directory' => $directory), WATCHDOG_ERROR);
    return FALSE;
  }

  foreach ($style['effects'] as $effect) {
    image_effect_apply($image, $effect);
  }

  if (!image_save($image, $destination)) {
    if (file_exists($destination)) {
      watchdog('image', 'Cached image file %destination already exists. There may be an issue with your rewrite configuration.', array('%destination' => $destination), WATCHDOG_ERROR);
    }
    return FALSE;
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
