# FileTransfer::removeDirectory()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 120–124 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L120-L124)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public final function removeDirectory($directory)
```

## Documentation

```text
Removes a directory.

@param $directory
  The directory to be removed.
```

## Code

```php
  public final function removeDirectory($directory) {
    $directory = $this->fixRemotePath($directory);
    $this->checkPath($directory);
    $this->removeDirectoryJailed($directory);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
