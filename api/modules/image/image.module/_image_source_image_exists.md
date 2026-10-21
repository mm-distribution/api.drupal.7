# _image_source_image_exists()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 942–968 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L942-L968)
- **Module/theme:** image

## Signature

```php
function _image_source_image_exists($image_uri, $token_is_valid)
```

## Documentation

```text
Checks whether the provided source image exists.

When a valid token is provided for the image URI, this function is
equivalent to calling file_exists($image_uri).

@param string $image_uri
  The URI for the source image.
@param bool $token_is_valid
  Whether a valid image token was supplied.

@return bool
  Whether the source image exists.
```

## Code

```php
function _image_source_image_exists($image_uri, $token_is_valid) {
  $exists = file_exists($image_uri);

  // If the file doesn't exist, we can stop here.
  if (!$exists) {
    return FALSE;
  }

  if ($token_is_valid) {
    return TRUE;
  }

  if (file_uri_scheme($image_uri) !== 'public') {
    return TRUE;
  }

  $image_path = drupal_realpath($image_uri);
  $private_path = variable_get('file_private_path', FALSE);
  if ($private_path) {
    $private_path = realpath($private_path);
    if ($private_path && strpos($image_path, $private_path) === 0) {
      return FALSE;
    }
  }

  return TRUE;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
