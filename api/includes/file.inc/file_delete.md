# file_delete()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1317–1349 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1317-L1349)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_delete(stdClass $file, $force = FALSE)
```

## Documentation

```text
Deletes a file and its database record.

If the $force parameter is not TRUE, file_usage_list() will be called to
determine if the file is being used by any modules. If the file is being
used the delete will be canceled.

@param $file
  A file object.
@param $force
  Boolean indicating that the file should be deleted even if the file is
  reported as in use by the file_usage table.

@return mixed
  TRUE for success, FALSE in the event of an error, or an array if the file
  is being used by any modules.

@see file_unmanaged_delete()
@see file_usage_list()
@see file_usage_delete()
@see hook_file_delete()
```

## Code

```php
function file_delete(stdClass $file, $force = FALSE) {
  if (!file_valid_uri($file->uri)) {
    if (($realpath = drupal_realpath($file->uri)) !== FALSE) {
      watchdog('file', 'File %file (%realpath) could not be deleted because it is not a valid URI. This may be caused by improper use of file_delete() or a missing stream wrapper.', array('%file' => $file->uri, '%realpath' => $realpath));
    }
    else {
      watchdog('file', 'File %file could not be deleted because it is not a valid URI. This may be caused by improper use of file_delete() or a missing stream wrapper.', array('%file' => $file->uri));
    }
    drupal_set_message(t('The specified file %file could not be deleted, because it is not a valid URI. More information is available in the system log.', array('%file' => $file->uri)), 'error');
    return FALSE;
  }

  // If any module still has a usage entry in the file_usage table, the file
  // will not be deleted, but file_delete() will return a populated array
  // that tests as TRUE.
  if (!$force && ($references = file_usage_list($file))) {
    return $references;
  }

  // Let other modules clean up any references to the deleted file.
  module_invoke_all('file_delete', $file);
  module_invoke_all('entity_delete', $file, 'file');

  // Make sure the file is deleted before removing its row from the
  // database, so UIs can still find the file in the database.
  if (file_unmanaged_delete($file->uri)) {
    db_delete('file_managed')->condition('fid', $file->fid)->execute();
    db_delete('file_usage')->condition('fid', $file->fid)->execute();
    entity_get_controller('file')->resetCache();
    return TRUE;
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
