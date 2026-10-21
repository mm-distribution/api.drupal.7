# _drupal_get_filename_perform_file_scan()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1074–1114 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1074-L1114)

## Signature

```php
function _drupal_get_filename_perform_file_scan($type, $name)
```

## Documentation

```text
Performs a file system scan to search for a system resource.

@param $type
  The type of the item (theme, theme_engine, module, profile).
@param $name
  The name of the item for which the filename is requested.

@return
  The filename of the requested item or FALSE if the item is not found.

@see drupal_get_filename()
@see _drupal_get_filename_fallback()
```

## Code

```php
function _drupal_get_filename_perform_file_scan($type, $name) {
  // The location of files will not change during the request, so do not use
  // drupal_static().
  static $dirs = array(), $files = array();

  // We have a consistent directory naming: modules, themes...
  $dir = $type . 's';
  if ($type == 'theme_engine') {
    $dir = 'themes/engines';
    $extension = 'engine';
  }
  elseif ($type == 'theme') {
    $extension = 'info';
  }
  else {
    $extension = $type;
  }

  // Check if we had already scanned this directory/extension combination.
  if (!isset($dirs[$dir][$extension])) {
    // Log that we have now scanned this directory/extension combination
    // into a static variable so as to prevent unnecessary file scans.
    $dirs[$dir][$extension] = TRUE;
    if (!function_exists('drupal_system_listing')) {
      require_once DRUPAL_ROOT . '/includes/common.inc';
    }
    // Scan the appropriate directories for all files with the requested
    // extension, not just the file we are currently looking for. This
    // prevents unnecessary scans from being repeated when this function is
    // called more than once in the same page request.
    $matches = drupal_system_listing("/^" . DRUPAL_PHP_FUNCTION_PATTERN . "\.$extension$/", $dir, 'name', 0);
    foreach ($matches as $matched_name => $file) {
      // Log the locations found in the file scan into a static variable.
      $files[$type][$matched_name] = $file->uri;
    }
  }

  // Return the results of the file system scan, or FALSE to indicate the file
  // was not found.
  return isset($files[$type][$name]) ? $files[$type][$name] : FALSE;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
