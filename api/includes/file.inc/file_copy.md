# file_copy()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 817–857 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L817-L857)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_copy(stdClass $source, $destination = NULL, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Copies a file to a new location and adds a file record to the database.

This function should be used when manipulating files that have records
stored in the database. This is a powerful function that in many ways
performs like an advanced version of copy().
- Checks if $source and $destination are valid and readable/writable.
- If file already exists in $destination either the call will error out,
  replace the file or rename the file based on the $replace parameter.
- If the $source and $destination are equal, the behavior depends on the
  $replace parameter. FILE_EXISTS_REPLACE will error out. FILE_EXISTS_RENAME
  will rename the file until the $destination is unique.
- Adds the new file to the files database. If the source file is a
  temporary file, the resulting file will also be a temporary file. See
  file_save_upload() for details on temporary files.

@param $source
  A file object.
@param $destination
  A string containing the destination that $source should be copied to.
  This must be a stream wrapper URI.
@param $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE - Replace the existing file. If a managed file with
      the destination name exists then its database entry will be updated. If
      no database entry is found then a new one will be created.
  - FILE_EXISTS_RENAME - Append _{incrementing number} until the filename is
      unique.
  - FILE_EXISTS_ERROR - Do nothing and return FALSE.

@return
  File object if the copy is successful, or FALSE in the event of an error.

@see file_unmanaged_copy()
@see hook_file_copy()
```

## Code

```php
function file_copy(stdClass $source, $destination = NULL, $replace = FILE_EXISTS_RENAME) {
  if (!file_valid_uri($destination)) {
    if (($realpath = drupal_realpath($source->uri)) !== FALSE) {
      watchdog('file', 'File %file (%realpath) could not be copied, because the destination %destination is invalid. This is often caused by improper use of file_copy() or a missing stream wrapper.', array('%file' => $source->uri, '%realpath' => $realpath, '%destination' => $destination));
    }
    else {
      watchdog('file', 'File %file could not be copied, because the destination %destination is invalid. This is often caused by improper use of file_copy() or a missing stream wrapper.', array('%file' => $source->uri, '%destination' => $destination));
    }
    drupal_set_message(t('The specified file %file could not be copied, because the destination is invalid. More information is available in the system log.', array('%file' => $source->uri)), 'error');
    return FALSE;
  }

  if ($uri = file_unmanaged_copy($source->uri, $destination, $replace)) {
    $file = clone $source;
    $file->fid = NULL;
    $file->uri = $uri;
    $file->filename = drupal_basename($uri);
    // If we are replacing an existing file re-use its database record.
    if ($replace == FILE_EXISTS_REPLACE) {
      $existing_files = file_load_multiple(array(), array('uri' => $uri));
      if (count($existing_files)) {
        $existing = reset($existing_files);
        $file->fid = $existing->fid;
        $file->filename = $existing->filename;
      }
    }
    // If we are renaming around an existing file (rather than a directory),
    // use its basename for the filename.
    elseif ($replace == FILE_EXISTS_RENAME && is_file($destination)) {
      $file->filename = drupal_basename($destination);
    }

    $file = file_save($file);

    // Inform modules that the file has been copied.
    module_invoke_all('file_copy', $file, $source);

    return $file;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
