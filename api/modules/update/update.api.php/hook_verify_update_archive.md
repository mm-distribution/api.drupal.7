# hook_verify_update_archive()

- **Type:** Hook (documentation function)
- **File:** [`modules/update/update.api.php`](_file.md), lines 122–129 · [local source](../../../../source/modules/update/update.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.api.php#L122-L129)
- **Module/theme:** update
- **Topics:** [hooks](../../../topics/hooks.md), [update_manager_file](../../../topics/update_manager_file.md)

## Signature

```php
function hook_verify_update_archive($project, $archive_file, $directory)
```

## Documentation

```text
Verify an archive after it has been downloaded and extracted.

@param string $project
  The short name of the project that has been downloaded.
@param string $archive_file
  The filename of the unextracted archive.
@param string $directory
  The directory that the archive was extracted into.

@return
  If there are any problems, return an array of error messages. If there are
  no problems, return an empty array.

@see update_manager_archive_verify()
@ingroup update_manager_file
```

## Code

```php
function hook_verify_update_archive($project, $archive_file, $directory) {
  $errors = array();
  if (!file_exists($directory)) {
    $errors[] = t('The %directory does not exist.', array('%directory' => $directory));
  }
  // Add other checks on the archive integrity here.
  return $errors;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_verify_update_archive()".

- [update_verify_update_archive()](../update.module/update_verify_update_archive.md) — `modules/update/update.module`

---
_Drupal 7.103 · [modules/update/update.api.php](https://github.com/drupal/drupal/blob/7.103/modules/update/update.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
