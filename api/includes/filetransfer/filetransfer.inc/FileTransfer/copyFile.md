# FileTransfer::copyFile()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 134–139 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L134-L139)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public final function copyFile($source, $destination)
```

## Documentation

```text
Copies a file.

@param $source
  The source file.
@param $destination
  The destination file.
```

## Code

```php
  public final function copyFile($source, $destination) {
    $source = $this->sanitizePath($source);
    $destination = $this->fixRemotePath($destination);
    $this->checkPath($destination);
    $this->copyFileJailed($source, $destination);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
