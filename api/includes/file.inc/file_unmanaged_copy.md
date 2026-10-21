# file_unmanaged_copy()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 915–985 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L915-L985)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_unmanaged_copy($source, $destination = NULL, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Copies a file to a new location without invoking the file API.

This is a powerful function that in many ways performs like an advanced
version of copy().
- Checks if $source and $destination are valid and readable/writable.
- If file already exists in $destination either the call will error out,
  replace the file or rename the file based on the $replace parameter.
- If the $source and $destination are equal, the behavior depends on the
  $replace parameter. FILE_EXISTS_REPLACE will error out. FILE_EXISTS_RENAME
  will rename the file until the $destination is unique.
- Provides a fallback using realpaths if the move fails using stream
  wrappers. This can occur because PHP's copy() function does not properly
  support streams if safe_mode or open_basedir are enabled. See
  https://bugs.php.net/bug.php?id=60456

@param $source
  A string specifying the filepath or URI of the source file.
@param $destination
  A URI containing the destination that $source should be copied to. The
  URI may be a bare filepath (without a scheme). If this value is omitted,
  Drupal's default files scheme will be used, usually "public://".
@param $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE - Replace the existing file.
  - FILE_EXISTS_RENAME - Append _{incrementing number} until the filename is
      unique.
  - FILE_EXISTS_ERROR - Do nothing and return FALSE.

@return
  The path to the new file, or FALSE in the event of an error.

@see file_copy()
```

## Code

```php
function file_unmanaged_copy($source, $destination = NULL, $replace = FILE_EXISTS_RENAME) {
  $original_source = $source;

  // Assert that the source file actually exists.
  if (!file_exists($source)) {
    // @todo Replace drupal_set_message() calls with exceptions instead.
    drupal_set_message(t('The specified file %file could not be copied, because no file by that name exists. Please check that you supplied the correct filename.', array('%file' => $original_source)), 'error');
    if (($realpath = drupal_realpath($original_source)) !== FALSE) {
      watchdog('file', 'File %file (%realpath) could not be copied because it does not exist.', array('%file' => $original_source, '%realpath' => $realpath));
    }
    else {
      watchdog('file', 'File %file could not be copied because it does not exist.', array('%file' => $original_source));
    }
    return FALSE;
  }

  // Build a destination URI if necessary.
  if (!isset($destination)) {
    $destination = file_build_uri(drupal_basename($source));
  }


  // Prepare the destination directory.
  if (file_prepare_directory($destination)) {
    // The destination is already a directory, so append the source basename.
    $destination = file_stream_wrapper_uri_normalize($destination . '/' . drupal_basename($source));
  }
  else {
    // Perhaps $destination is a dir/file?
    $dirname = drupal_dirname($destination);
    if (!file_prepare_directory($dirname)) {
      // The destination is not valid.
      watchdog('file', 'File %file could not be copied, because the destination directory %destination is not configured correctly.', array('%file' => $original_source, '%destination' => $dirname));
      drupal_set_message(t('The specified file %file could not be copied, because the destination directory is not properly configured. This may be caused by a problem with file or directory permissions. More information is available in the system log.', array('%file' => $original_source)), 'error');
      return FALSE;
    }
  }

  // Determine whether we can perform this operation based on overwrite rules.
  $destination = file_destination($destination, $replace);
  if ($destination === FALSE) {
    drupal_set_message(t('The file %file could not be copied because a file by that name already exists in the destination directory.', array('%file' => $original_source)), 'error');
    watchdog('file', 'File %file could not be copied because a file by that name already exists in the destination directory (%directory)', array('%file' => $original_source, '%directory' => $destination));
    return FALSE;
  }

  // Assert that the source and destination filenames are not the same.
  $real_source = drupal_realpath($source);
  $real_destination = drupal_realpath($destination);
  if ($source == $destination || ($real_source !== FALSE) && ($real_source == $real_destination)) {
    drupal_set_message(t('The specified file %file was not copied because it would overwrite itself.', array('%file' => $source)), 'error');
    watchdog('file', 'File %file could not be copied because it would overwrite itself.', array('%file' => $source));
    return FALSE;
  }
  // Make sure the .htaccess files are present.
  file_ensure_htaccess();
  // Perform the copy operation.
  if (!@copy($source, $destination)) {
    // If the copy failed and realpaths exist, retry the operation using them
    // instead.
    if ($real_source === FALSE || $real_destination === FALSE || !@copy($real_source, $real_destination)) {
      watchdog('file', 'The specified file %file could not be copied to %destination.', array('%file' => $source, '%destination' => $destination), WATCHDOG_ERROR);
      return FALSE;
    }
  }

  // Set the permissions on the new file.
  drupal_chmod($destination);

  return $destination;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
