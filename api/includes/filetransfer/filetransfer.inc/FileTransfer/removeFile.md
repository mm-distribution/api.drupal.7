# FileTransfer::removeFile()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 147–151 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L147-L151)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public final function removeFile($destination)
```

## Documentation

```text
Removes a file.

@param $destination
  The destination file to be removed.
```

## Code

```php
  public final function removeFile($destination) {
    $destination = $this->fixRemotePath($destination);
    $this->checkPath($destination);
    $this->removeFileJailed($destination);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
