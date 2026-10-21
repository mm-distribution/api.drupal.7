# file_prepare_directory()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 439–461 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L439-L461)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_prepare_directory(&$directory, $options = FILE_MODIFY_PERMISSIONS)
```

## Documentation

```text
Checks that the directory exists and is writable.

Directories need to have execute permissions to be considered a directory by
FTP servers, etc.

@param $directory
  A string reference containing the name of a directory path or URI. A
  trailing slash will be trimmed from a path.
@param $options
  A bitmask to indicate if the directory should be created if it does
  not exist (FILE_CREATE_DIRECTORY) or made writable if it is read-only
  (FILE_MODIFY_PERMISSIONS).

@return
  TRUE if the directory exists (or was created) and is writable. FALSE
  otherwise.
```

## Code

```php
function file_prepare_directory(&$directory, $options = FILE_MODIFY_PERMISSIONS) {
  if (!file_stream_wrapper_valid_scheme(file_uri_scheme($directory))) {
    // Only trim if we're not dealing with a stream.
    $directory = rtrim($directory, '/\\');
  }

  // Check if directory exists.
  if (!is_dir($directory)) {
    // Let drupal_mkdir() recursively create directories and use the default
    // directory permissions.
    if ($options & FILE_CREATE_DIRECTORY) {
      return @drupal_mkdir($directory, NULL, TRUE);
    }
    return FALSE;
  }
  // The directory exists, so check to see if it is writable.
  $writable = is_writable($directory);
  if (!$writable && ($options & FILE_MODIFY_PERMISSIONS)) {
    return drupal_chmod($directory);
  }

  return $writable;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
