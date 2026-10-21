# file_test_file_url_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 323–412 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L323-L412)
- **Module/theme:** batch_test
- **Implements:** [hook_file_url_alter()](../../../system/system.api.php/hook_file_url_alter.md)

## Signature

```php
function file_test_file_url_alter(&$uri)
```

## Documentation

```text
Implements hook_file_url_alter().
```

## Code

```php
function file_test_file_url_alter(&$uri) {
  // Only run this hook when this variable is set. Otherwise, we'd have to add
  // another hidden test module just for this hook.
  $alter_mode = variable_get('file_test_hook_file_url_alter', FALSE);
  if (!$alter_mode) {
    return;
  }
  // Test alteration of file URLs to use a CDN.
  elseif ($alter_mode == 'cdn') {
    $cdn_extensions = array('css', 'js', 'gif', 'jpg', 'jpeg', 'png');

    // Most CDNs don't support private file transfers without a lot of hassle,
    // so don't support this in the common case.
    $schemes = array('public');

    $scheme = file_uri_scheme($uri);

    // Only serve shipped files and public created files from the CDN.
    if (!$scheme || in_array($scheme, $schemes)) {
      // Shipped files.
      if (!$scheme) {
        $path = $uri;
      }
      // Public created files.
      else {
        $wrapper = file_stream_wrapper_get_instance_by_scheme($scheme);
        $path = $wrapper->getDirectoryPath() . '/' . file_uri_target($uri);
      }

      // Clean up Windows paths.
      $path = str_replace('\\', '/', $path);

      // Serve files with one of the CDN extensions from CDN 1, all others from
      // CDN 2.
      $pathinfo = pathinfo($path);
      if (array_key_exists('extension', $pathinfo) && in_array($pathinfo['extension'], $cdn_extensions)) {
        $uri = FILE_URL_TEST_CDN_1 . '/' . $path;
      }
      else {
        $uri = FILE_URL_TEST_CDN_2 . '/' . $path;
      }
    }
  }
  // Test alteration of file URLs to use root-relative URLs.
  elseif ($alter_mode == 'root-relative') {
    // Only serve shipped files and public created files with root-relative
    // URLs.
    $scheme = file_uri_scheme($uri);
    if (!$scheme || $scheme == 'public') {
      // Shipped files.
      if (!$scheme) {
        $path = $uri;
      }
      // Public created files.
      else {
        $wrapper = file_stream_wrapper_get_instance_by_scheme($scheme);
        $path = $wrapper->getDirectoryPath() . '/' . file_uri_target($uri);
      }

      // Clean up Windows paths.
      $path = str_replace('\\', '/', $path);

      // Generate a root-relative URL.
      $uri = base_path() . '/' . $path;
    }
  }
  // Test alteration of file URLs to use protocol-relative URLs.
  elseif ($alter_mode == 'protocol-relative') {
    // Only serve shipped files and public created files with protocol-relative
    // URLs.
    $scheme = file_uri_scheme($uri);
    if (!$scheme || $scheme == 'public') {
      // Shipped files.
      if (!$scheme) {
        $path = $uri;
      }
      // Public created files.
      else {
        $wrapper = file_stream_wrapper_get_instance_by_scheme($scheme);
        $path = $wrapper->getDirectoryPath() . '/' . file_uri_target($uri);
      }

      // Clean up Windows paths.
      $path = str_replace('\\', '/', $path);

      // Generate a protocol-relative URL.
      $uri = '/' . base_path() . '/' . $path;
    }
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
