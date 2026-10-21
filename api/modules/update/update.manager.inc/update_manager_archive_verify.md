# update_manager_archive_verify()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 816–818 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L816-L818)
- **Module/theme:** update
- **Topics:** [update_manager_file](../../../topics/update_manager_file.md)

## Signature

```php
function update_manager_archive_verify($project, $archive_file, $directory)
```

## Documentation

```text
Verifies an archive after it has been downloaded and extracted.

This function is responsible for invoking hook_verify_update_archive().

@param string $project
  The short name of the project to download.
@param string $archive_file
  The filename of the unextracted archive.
@param string $directory
  The directory that the archive was extracted into.

@return array
  An array of error messages to display if the archive was invalid. If there
  are no errors, it will be an empty array.
```

## Code

```php
function update_manager_archive_verify($project, $archive_file, $directory) {
  return module_invoke_all('verify_update_archive', $project, $archive_file, $directory);
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
