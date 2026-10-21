# file_save()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 626–657 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L626-L657)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_save(stdClass $file)
```

## Documentation

```text
Saves a file object to the database.

If the $file->fid is not set a new record will be added.

@param $file
  A file object returned by file_load().

@return
  The updated file object.

@see hook_file_insert()
@see hook_file_update()
```

## Code

```php
function file_save(stdClass $file) {
  $file->timestamp = REQUEST_TIME;
  $file->filesize = filesize($file->uri);

  // Load the stored entity, if any.
  if (!empty($file->fid) && !isset($file->original)) {
    $file->original = entity_load_unchanged('file', $file->fid);
  }

  module_invoke_all('file_presave', $file);
  module_invoke_all('entity_presave', $file, 'file');

  if (empty($file->fid)) {
    drupal_write_record('file_managed', $file);
    // Inform modules about the newly added file.
    module_invoke_all('file_insert', $file);
    module_invoke_all('entity_insert', $file, 'file');
  }
  else {
    drupal_write_record('file_managed', $file, 'fid');
    // Inform modules that the file has been updated.
    module_invoke_all('file_update', $file);
    module_invoke_all('entity_update', $file, 'file');
  }

  // Clear internal properties.
  unset($file->original);
  // Clear the static loading cache.
  entity_get_controller('file')->resetCache(array($file->fid));

  return $file;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
