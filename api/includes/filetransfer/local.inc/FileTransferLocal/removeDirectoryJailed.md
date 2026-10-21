# FileTransferLocal::removeDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 28–48 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L28-L48)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
protected function removeDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function removeDirectoryJailed($directory) {
    if (!is_dir($directory)) {
      // Programmer error assertion, not something we expect users to see.
      throw new FileTransferException('removeDirectoryJailed() called with a path (%directory) that is not a directory.', NULL, array('%directory' => $directory));
    }
    foreach (new RecursiveIteratorIterator(new SkipDotsRecursiveDirectoryIterator($directory), RecursiveIteratorIterator::CHILD_FIRST) as $filename => $file) {
      if ($file->isDir()) {
        if (@!drupal_rmdir($filename)) {
          throw new FileTransferException('Cannot remove directory %directory.', NULL, array('%directory' => $filename));
        }
      }
      elseif ($file->isFile()) {
        if (@!drupal_unlink($filename)) {
          throw new FileTransferException('Cannot remove file %file.', NULL, array('%file' => $filename));
        }
      }
    }
    if (@!drupal_rmdir($directory)) {
      throw new FileTransferException('Cannot remove directory %directory.', NULL, array('%directory' => $directory));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
