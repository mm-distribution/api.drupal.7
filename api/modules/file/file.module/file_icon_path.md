# file_icon_path()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 904–942 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L904-L942)
- **Module/theme:** file

## Signature

```php
function file_icon_path($file, $icon_directory = NULL)
```

## Documentation

```text
Creates a path to the icon for a file object.

@param $file
  A file object.
@param $icon_directory
  (optional) A path to a directory of icons to be used for files. Defaults to
  the value of the "file_icon_directory" variable.

@return
  A string to the icon as a local path, or FALSE if an appropriate icon could
  not be found.
```

## Code

```php
function file_icon_path($file, $icon_directory = NULL) {
  // Use the default set of icons if none specified.
  if (!isset($icon_directory)) {
    $icon_directory = variable_get('file_icon_directory', drupal_get_path('module', 'file') . '/icons');
  }

  // If there's an icon matching the exact mimetype, go for it.
  $dashed_mime = strtr($file->filemime, array('/' => '-'));
  $icon_path = $icon_directory . '/' . $dashed_mime . '.png';
  if (file_exists($icon_path)) {
    return $icon_path;
  }

  // For a few mimetypes, we can "manually" map to a generic icon.
  $generic_mime = (string) file_icon_map($file);
  $icon_path = $icon_directory . '/' . $generic_mime . '.png';
  if ($generic_mime && file_exists($icon_path)) {
    return $icon_path;
  }

  // Use generic icons for each category that provides such icons.
  foreach (array('audio', 'image', 'text', 'video') as $category) {
    if (strpos($file->filemime, $category . '/') === 0) {
      $icon_path = $icon_directory . '/' . $category . '-x-generic.png';
      if (file_exists($icon_path)) {
        return $icon_path;
      }
    }
  }

  // Try application-octet-stream as last fallback.
  $icon_path = $icon_directory . '/application-octet-stream.png';
  if (file_exists($icon_path)) {
    return $icon_path;
  }

  // No icon can be found.
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
