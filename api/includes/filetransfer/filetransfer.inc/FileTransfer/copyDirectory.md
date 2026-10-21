# FileTransfer::copyDirectory()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 78–83 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L78-L83)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public final function copyDirectory($source, $destination)
```

## Documentation

```text
Copies a directory.

@param $source
  The source path.
@param $destination
  The destination path.
```

## Code

```php
  public final function copyDirectory($source, $destination) {
    $source = $this->sanitizePath($source);
    $destination = $this->fixRemotePath($destination);
    $this->checkPath($destination);
    $this->copyDirectoryJailed($source, $destination);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
