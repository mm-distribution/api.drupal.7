# file_validate_is_image()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1860–1869 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1860-L1869)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_validate_is_image(stdClass $file)
```

## Documentation

```text
Checks that the file is recognized by image_get_info() as an image.

@param $file
  A Drupal file object.

@return
  An array. If the file is not an image, it will contain an error message.

@see hook_file_validate()
```

## Code

```php
function file_validate_is_image(stdClass $file) {
  $errors = array();

  $info = image_get_info($file->uri);
  if (!$info || empty($info['extension'])) {
    $errors[] = t('The image file is invalid or the image type is not allowed. Allowed types: %allowed_types', array('%allowed_types' => t('Only JPEG, PNG and GIF images are allowed.')));
  }

  return $errors;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
