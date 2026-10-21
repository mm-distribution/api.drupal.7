# FileTransfer::createDirectory()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 108–112 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L108-L112)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public final function createDirectory($directory)
```

## Documentation

```text
Creates a directory.

@param $directory
  The directory to be created.
```

## Code

```php
  public final function createDirectory($directory) {
    $directory = $this->fixRemotePath($directory);
    $this->checkPath($directory);
    $this->createDirectoryJailed($directory);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
