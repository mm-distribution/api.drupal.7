# image_save()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 417–431 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L417-L431)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_save(stdClass $image, $destination = NULL)
```

## Documentation

```text
Closes the image and saves the changes to a file.

@param $image
  An image object returned by image_load(). The object's 'info' property
  will be updated if the file is saved successfully.
@param $destination
  Destination path where the image should be saved. If it is empty the
  original image file will be overwritten.

@return
  TRUE on success, FALSE on failure.

@see image_load()
@see image_gd_save()
```

## Code

```php
function image_save(stdClass $image, $destination = NULL) {
  if (empty($destination)) {
    $destination = $image->source;
  }
  if ($return = image_toolkit_invoke('save', $image, array($destination))) {
    // Clear the cached file size and refresh the image information.
    clearstatcache();
    $image->info = image_get_info($destination, $image->toolkit);

    if (drupal_chmod($destination)) {
      return $return;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
