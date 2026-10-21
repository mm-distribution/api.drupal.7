# file_icon_url()

- **Type:** Function
- **File:** [`modules/file/file.module`](_file.md), lines 884–889 · [local source](../../../../source/modules/file/file.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module#L884-L889)
- **Module/theme:** file

## Signature

```php
function file_icon_url($file, $icon_directory = NULL)
```

## Documentation

```text
Creates a URL to the icon for a file object.

@param $file
  A file object.
@param $icon_directory
  (optional) A path to a directory of icons to be used for files. Defaults to
  the value of the "file_icon_directory" variable.

@return
  A URL string to the icon, or FALSE if an appropriate icon cannot be found.
```

## Code

```php
function file_icon_url($file, $icon_directory = NULL) {
  if ($icon_path = file_icon_path($file, $icon_directory)) {
    return base_path() . $icon_path;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/file/file.module](https://github.com/drupal/drupal/blob/7.103/modules/file/file.module) · Licensed GPL-2.0-or-later (see LICENSE)._
