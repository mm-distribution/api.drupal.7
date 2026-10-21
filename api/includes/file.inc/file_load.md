# file_load()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 607–610 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L607-L610)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_load($fid)
```

## Documentation

```text
Loads a single file object from the database.

@param $fid
  A file ID.

@return
  An object representing the file, or FALSE if the file was not found.

@see hook_file_load()
@see file_load_multiple()
```

## Code

```php
function file_load($fid) {
  $files = file_load_multiple(array($fid), array());
  return reset($files);
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
