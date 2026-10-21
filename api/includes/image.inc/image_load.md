# image_load()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 383–399 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L383-L399)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_load($file, $toolkit = FALSE)
```

## Documentation

```text
Loads an image file and returns an image object.

Any changes to the file are not saved until image_save() is called.

@param $file
  Path to an image file.
@param $toolkit
  An optional, image toolkit name to override the default.

@return
  An image object or FALSE if there was a problem loading the file. The
  image object has the following properties:
   - 'source' - The original file path.
   - 'info' - The array of information returned by image_get_info()
   - 'toolkit' - The name of the image toolkit requested when the image was
     loaded.
  Image toolkits may add additional properties. The caller is advised not to
  monkey about with them.

@see image_save()
@see image_get_info()
@see image_get_available_toolkits()
@see image_gd_load()
```

## Code

```php
function image_load($file, $toolkit = FALSE) {
  if (!$toolkit) {
    $toolkit = image_get_toolkit();
  }
  if ($toolkit) {
    $image = new stdClass();
    $image->source = $file;
    $image->info = image_get_info($file, $toolkit);
    if (isset($image->info) && is_array($image->info)) {
      $image->toolkit = $toolkit;
      if (image_toolkit_invoke('load', $image)) {
        return $image;
      }
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
