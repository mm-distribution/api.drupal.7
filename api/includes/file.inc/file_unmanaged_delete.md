# file_unmanaged_delete()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1367–1385 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1367-L1385)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_unmanaged_delete($path)
```

## Documentation

```text
Deletes a file without database changes or hook invocations.

This function should be used when the file to be deleted does not have an
entry recorded in the files table.

@param $path
  A string containing a file path or (streamwrapper) URI.

@return
  TRUE for success or path does not exist, or FALSE in the event of an
  error.

@see file_delete()
@see file_unmanaged_delete_recursive()
```

## Code

```php
function file_unmanaged_delete($path) {
  if (is_dir($path)) {
    watchdog('file', '%path is a directory and cannot be removed using file_unmanaged_delete().', array('%path' => $path), WATCHDOG_ERROR);
    return FALSE;
  }
  if (is_file($path)) {
    return drupal_unlink($path);
  }
  // Return TRUE for non-existent file, but log that nothing was actually
  // deleted, as the current state is the intended result.
  if (!file_exists($path)) {
    watchdog('file', 'The file %path was not deleted, because it does not exist.', array('%path' => $path), WATCHDOG_NOTICE);
    return TRUE;
  }
  // We cannot handle anything other than files and directories. Log an error
  // for everything else (sockets, symbolic links, etc).
  watchdog('file', 'The file %path is not of a recognized type so it was not deleted.', array('%path' => $path), WATCHDOG_ERROR);
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
