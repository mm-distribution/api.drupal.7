# _system_theme_settings_validate_path()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 672–689 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L672-L689)
- **Module/theme:** system

## Signature

```php
function _system_theme_settings_validate_path($path)
```

## Documentation

```text
Helper function for the system_theme_settings form.

Attempts to validate normal system paths, paths relative to the public files
directory, or stream wrapper URIs. If the given path is any of the above,
returns a valid path or URI that the theme system can display.

@param $path
  A path relative to the Drupal root or to the public files directory, or
  a stream wrapper URI.
@return mixed
  A valid path that can be displayed through the theme system, or FALSE if
  the path could not be validated.
```

## Code

```php
function _system_theme_settings_validate_path($path) {
  // Absolute local file paths are invalid.
  if (drupal_realpath($path) == $path) {
    return FALSE;
  }
  // A path relative to the Drupal root or a fully qualified URI is valid.
  if (is_file($path)) {
    return $path;
  }
  // Prepend 'public://' for relative file paths within public filesystem.
  if (file_uri_scheme($path) === FALSE) {
    $path = 'public://' . $path;
  }
  if (is_file($path)) {
    return $path;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
