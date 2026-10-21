# image_file_download()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 280–325 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L280-L325)
- **Module/theme:** image
- **Implements:** [hook_file_download()](../../system/system.api.php/hook_file_download.md)

## Signature

```php
function image_file_download($uri)
```

## Documentation

```text
Implements hook_file_download().

Control the access to files underneath the styles directory.
```

## Code

```php
function image_file_download($uri) {
  $path = file_uri_target($uri);

  // Private file access for image style derivatives.
  if (strpos($path, 'styles/') === 0) {
    $args = explode('/', $path);
    // Discard the first part of the path (styles).
    array_shift($args);
    // Get the style name from the second part.
    $style_name = array_shift($args);
    // Remove the scheme from the path.
    array_shift($args);

    // Then the remaining parts are the path to the image.
    $original_uri = file_uri_scheme($uri) . '://' . implode('/', $args);

    // Check that the file exists and is an image.
    if ($info = image_get_info($uri)) {
      // Check the permissions of the original to grant access to this image.
      $headers = module_invoke_all('file_download', $original_uri);
      // Confirm there's at least one module granting access and none denying access.
      if (!empty($headers) && !in_array(-1, $headers)) {
        return array(
          // Send headers describing the image's size, and MIME-type...
          'Content-Type' => $info['mime_type'],
          'Content-Length' => $info['file_size'],
          // By not explicitly setting them here, this uses normal Drupal
          // Expires, Cache-Control and ETag headers to prevent proxy or
          // browser caching of private images.
        );
      }
    }
    return -1;
  }

  // Private file access for the original files. Note that we only check access
  // for non-temporary images, since file.module will grant access for all
  // temporary files.
  $files = file_load_multiple(array(), array('uri' => $uri));
  if (count($files)) {
    $file = reset($files);
    if ($file->status) {
      return file_file_download($uri, 'image');
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
