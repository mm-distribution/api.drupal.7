# update_clear_update_disk_cache()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 958–970 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L958-L970)
- **Module/theme:** update

## Signature

```php
function update_clear_update_disk_cache()
```

## Documentation

```text
Clears the temporary files and directories based on file age from disk.
```

## Code

```php
function update_clear_update_disk_cache() {
  // List of update module cache directories. Do not create the directories if
  // they do not exist.
  $directories = array(
    _update_manager_cache_directory(FALSE),
    _update_manager_extract_directory(FALSE),
  );

  // Search for files and directories in base folder only without recursion.
  foreach ($directories as $directory) {
    file_scan_directory($directory, '/.*/', array('callback' => 'update_delete_file_if_stale', 'recurse' => FALSE));
  }
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
