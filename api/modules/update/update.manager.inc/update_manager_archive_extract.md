# update_manager_archive_extract()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 775–798 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L775-L798)
- **Module/theme:** update
- **Topics:** [update_manager_file](../../../topics/update_manager_file.md)

## Signature

```php
function update_manager_archive_extract($file, $directory)
```

## Documentation

```text
Unpacks a downloaded archive file.

@param string $file
  The filename of the archive you wish to extract.
@param string $directory
  The directory you wish to extract the archive into.

@return Archiver
  The Archiver object used to extract the archive.

@throws Exception
```

## Code

```php
function update_manager_archive_extract($file, $directory) {
  $archiver = archiver_get_archiver($file);
  if (!$archiver) {
    throw new Exception(t('Cannot extract %file, not a valid archive.', array ('%file' => $file)));
  }

  // Remove the directory if it exists, otherwise it might contain a mixture of
  // old files mixed with the new files (e.g. in cases where files were removed
  // from a later release).
  $files = $archiver->listContents();

  // Unfortunately, we can only use the directory name to determine the project
  // name. Some archivers list the first file as the directory (i.e., MODULE/)
  // and others list an actual file (i.e., MODULE/README.TXT).
  $project = strtok($files[0], '/\\');

  $extract_location = $directory . '/' . $project;
  if (file_exists($extract_location)) {
    file_unmanaged_delete_recursive($extract_location);
  }

  $archiver->extract($directory);
  return $archiver;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
