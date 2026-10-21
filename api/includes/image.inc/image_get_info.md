# image_get_info()

- **Type:** Function
- **File:** [`includes/image.inc`](_file.md), lines 124–144 · [local source](../../../source/includes/image.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L124-L144)
- **Topics:** [image](../../topics/image.md)

## Signature

```php
function image_get_info($filepath, $toolkit = FALSE)
```

## Documentation

```text
Gets details about an image.

Drupal supports GIF, JPG and PNG file formats when used with the GD
toolkit, and may support others, depending on which toolkits are
installed.

@param $filepath
  String specifying the path of the image file.
@param $toolkit
  An optional image toolkit name to override the default.

@return
  FALSE, if the file could not be found or is not an image. Otherwise, a
  keyed array containing information about the image:
  - "width": Width, in pixels.
  - "height": Height, in pixels.
  - "extension": Commonly used file extension for the image.
  - "mime_type": MIME type ('image/jpeg', 'image/gif', 'image/png').
  - "file_size": File size in bytes.
```

## Code

```php
function image_get_info($filepath, $toolkit = FALSE) {
  $details = FALSE;
  if (!is_file($filepath) && !is_uploaded_file($filepath)) {
    return $details;
  }

  if (!$toolkit) {
    $toolkit = image_get_toolkit();
  }
  if ($toolkit) {
    $image = new stdClass();
    $image->source = $filepath;
    $image->toolkit = $toolkit;
    $details = image_toolkit_invoke('get_info', $image);
    if (isset($details) && is_array($details)) {
      $details['file_size'] = filesize($filepath);
    }
  }

  return $details;
}
```

---
_Drupal 7.103 · [includes/image.inc](https://github.com/drupal/drupal/blob/7.103/includes/image.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
