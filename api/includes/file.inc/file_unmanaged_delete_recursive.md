# file_unmanaged_delete_recursive()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 1408–1423 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L1408-L1423)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_unmanaged_delete_recursive($path)
```

## Documentation

```text
Deletes all files and directories in the specified filepath recursively.

If the specified path is a directory then the function will call itself
recursively to process the contents. Once the contents have been removed the
directory will also be removed.

If the specified path is a file then it will be passed to
file_unmanaged_delete().

Note that this only deletes visible files with write permission.

@param $path
  A string containing either an URI or a file or directory path.

@return
  TRUE for success or if path does not exist, FALSE in the event of an
  error.

@see file_unmanaged_delete()
```

## Code

```php
function file_unmanaged_delete_recursive($path) {
  if (is_dir($path)) {
    $dir = dir($path);
    while (($entry = $dir->read()) !== FALSE) {
      if ($entry == '.' || $entry == '..') {
        continue;
      }
      $entry_path = $path . '/' . $entry;
      file_unmanaged_delete_recursive($entry_path);
    }
    $dir->close();

    return drupal_rmdir($path);
  }
  return file_unmanaged_delete($path);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
