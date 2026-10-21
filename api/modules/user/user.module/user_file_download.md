# user_file_download()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 913–918 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L913-L918)
- **Module/theme:** user
- **Implements:** [hook_file_download()](../../system/system.api.php/hook_file_download.md)

## Signature

```php
function user_file_download($uri)
```

## Documentation

```text
Implements hook_file_download().

Ensure that user pictures (avatars) are always downloadable.
```

## Code

```php
function user_file_download($uri) {
  if (strpos(file_uri_target($uri), variable_get('user_picture_path', 'pictures') . '/picture-') === 0) {
    $info = image_get_info($uri);
    return array('Content-Type' => $info['mime_type']);
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
