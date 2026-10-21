# hook_file_download()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3006–3021 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3006-L3021)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_file_download($uri)
```

## Documentation

```text
Control access to private file downloads and specify HTTP headers.

This hook allows modules enforce permissions on file downloads when the
private file download method is selected. Modules can also provide headers
to specify information like the file's name or MIME type.

@param $uri
  The URI of the file.
@return
  If the user does not have permission to access the file, return -1. If the
  user has permission, return an array with the appropriate headers. If the
  file is not controlled by the current module, the return value should be
  NULL.

@see file_download()
```

## Code

```php
function hook_file_download($uri) {
  // Check if the file is controlled by the current module.
  if (!file_prepare_directory($uri)) {
    $uri = FALSE;
  }
  if (strpos(file_uri_target($uri), variable_get('user_picture_path', 'pictures') . '/picture-') === 0) {
    if (!user_access('access user profiles')) {
      // Access to the file is denied.
      return -1;
    }
    else {
      $info = image_get_info($uri);
      return array('Content-Type' => $info['mime_type']);
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_file_download()".

- [file_test_file_download()](../../simpletest/tests/file_test.module/file_test_file_download.md) — `modules/simpletest/tests/file_test.module`
- [file_file_download()](../../file/file.module/file_file_download.md) — `modules/file/file.module`
- [file_module_test_file_download()](../../file/tests/file_module_test.module/file_module_test_file_download.md) — `modules/file/tests/file_module_test.module`
- [image_file_download()](../../image/image.module/image_file_download.md) — `modules/image/image.module`
- [system_file_download()](../system.module/system_file_download.md) — `modules/system/system.module`
- [user_file_download()](../../user/user.module/user_file_download.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
