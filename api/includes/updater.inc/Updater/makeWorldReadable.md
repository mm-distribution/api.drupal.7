# Updater::makeWorldReadable()

- **Type:** Method
- **File:** [`includes/updater.inc`](../_file.md), lines 360–366 · [local source](../../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L360-L366)
- **Class:** [Updater](../Updater.md)

## Signature

```php
public function makeWorldReadable(&$filetransfer, $path, $recursive = TRUE)
```

## Documentation

```text
Ensure that a given directory is world readable.

@param FileTransfer $filetransfer
  Object which is a child of FileTransfer.
@param string $path
  The file path to make world readable.
@param bool $recursive
  If the chmod should be applied recursively.
```

## Code

```php
  public function makeWorldReadable(&$filetransfer, $path, $recursive = TRUE) {
    if (!is_executable($path)) {
      // Set it to read + execute.
      $new_perms = substr(sprintf('%o', fileperms($path)), -4, -1) . "5";
      $filetransfer->chmod($path, intval($new_perms, 8), $recursive);
    }
  }
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
