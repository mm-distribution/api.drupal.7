# file_move()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1071–1116 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1071-L1116)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_move(stdClass $source, $destination = NULL, $replace = FILE_EXISTS_RENAME)
```

## Documentation

```text
Moves a file to a new location and update the file's database entry.

Moving a file is performed by copying the file to the new location and then
deleting the original.
- Checks if $source and $destination are valid and readable/writable.
- Performs a file move if $source is not equal to $destination.
- If file already exists in $destination either the call will error out,
  replace the file or rename the file based on the $replace parameter.
- Adds the new file to the files database.

@param $source
  A file object.
@param $destination
  A string containing the destination that $source should be moved to.
  This must be a stream wrapper URI.
@param $replace
  Replace behavior when the destination file already exists:
  - FILE_EXISTS_REPLACE - Replace the existing file. If a managed file with
      the destination name exists then its database entry will be updated and
      file_delete() called on the source file after hook_file_move is called.
      If no database entry is found then the source files record will be
      updated.
  - FILE_EXISTS_RENAME - Append _{incrementing number} until the filename is
      unique.
  - FILE_EXISTS_ERROR - Do nothing and return FALSE.

@return
  Resulting file object for success, or FALSE in the event of an error.

@see file_unmanaged_move()
@see hook_file_move()
```

## Code

```php
function file_move(stdClass $source, $destination = NULL, $replace = FILE_EXISTS_RENAME) {
  if (!file_valid_uri($destination)) {
    if (($realpath = drupal_realpath($source->uri)) !== FALSE) {
      watchdog('file', 'File %file (%realpath) could not be moved, because the destination %destination is invalid. This may be caused by improper use of file_move() or a missing stream wrapper.', array('%file' => $source->uri, '%realpath' => $realpath, '%destination' => $destination));
    }
    else {
      watchdog('file', 'File %file could not be moved, because the destination %destination is invalid. This may be caused by improper use of file_move() or a missing stream wrapper.', array('%file' => $source->uri, '%destination' => $destination));
    }
    drupal_set_message(t('The specified file %file could not be moved, because the destination is invalid. More information is available in the system log.', array('%file' => $source->uri)), 'error');
    return FALSE;
  }

  if ($uri = file_unmanaged_move($source->uri, $destination, $replace)) {
    $delete_source = FALSE;

    $file = clone $source;
    $file->uri = $uri;
    // If we are replacing an existing file re-use its database record.
    if ($replace == FILE_EXISTS_REPLACE) {
      $existing_files = file_load_multiple(array(), array('uri' => $uri));
      if (count($existing_files)) {
        $existing = reset($existing_files);
        $delete_source = TRUE;
        $file->fid = $existing->fid;
      }
    }
    // If we are renaming around an existing file (rather than a directory),
    // use its basename for the filename.
    elseif ($replace == FILE_EXISTS_RENAME && is_file($destination)) {
      $file->filename = drupal_basename($destination);
    }

    $file = file_save($file);

    // Inform modules that the file has been moved.
    module_invoke_all('file_move', $file, $source);

    if ($delete_source) {
      // Try a soft delete to remove original if it's not in use elsewhere.
      file_delete($source);
    }

    return $file;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
