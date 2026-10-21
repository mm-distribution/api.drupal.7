# file_module_test_file_download()

- **Type:** Function
- **File:** [`modules/file/tests/file_module_test.module`](_file.md), lines 74–84 · [local source](../../../../../source/modules/file/tests/file_module_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module#L74-L84)
- **Module/theme:** file_module_test
- **Implements:** [hook_file_download()](../../../system/system.api.php/hook_file_download.md)

## Signature

```php
function file_module_test_file_download($uri)
```

## Documentation

```text
Implements hook_file_download().
```

## Code

```php
function file_module_test_file_download($uri) {
  if (variable_get('file_module_test_grant_download_access')) {
    // Mimic what file_get_content_headers() would do if we had a full $file
    // object to pass to it.
    return array(
      'Content-Type' => mime_header_encode(file_get_mimetype($uri)),
      'Content-Length' => filesize($uri),
      'Cache-Control' => 'private',
    );
  }
}
```

---
_Drupal 7.103 · [modules/file/tests/file_module_test.module](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file_module_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
