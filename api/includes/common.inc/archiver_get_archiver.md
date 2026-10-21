# archiver_get_archiver()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8614–8634 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8614-L8634)

## Signature

```php
function archiver_get_archiver($file)
```

## Documentation

```text
Creates the appropriate archiver for the specified file.

@param $file
  The full path of the archive file. Note that stream wrapper paths are
  supported, but not remote ones.

@return
  A newly created instance of the archiver class appropriate
  for the specified file, already bound to that file.
  If no appropriate archiver class was found, will return FALSE.
```

## Code

```php
function archiver_get_archiver($file) {
  // Archivers can only work on local paths
  $filepath = drupal_realpath($file);
  if (!is_file($filepath)) {
    throw new Exception(t('Archivers can only operate on local files: %file not supported', array('%file' => $file)));
  }
  $archiver_info = archiver_get_info();

  foreach ($archiver_info as $implementation) {
    foreach ($implementation['extensions'] as $extension) {
      // Because extensions may be multi-part, such as .tar.gz,
      // we cannot use simpler approaches like substr() or pathinfo().
      // This method isn't quite as clean but gets the job done.
      // Also note that the file may not yet exist, so we cannot rely
      // on fileinfo() or other disk-level utilities.
      if (strrpos($filepath, '.' . $extension) === strlen($filepath) - strlen('.' . $extension)) {
        return new $implementation['class']($filepath);
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
