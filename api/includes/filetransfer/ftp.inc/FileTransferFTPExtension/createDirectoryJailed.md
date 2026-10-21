# FileTransferFTPExtension::createDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 70–74 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L70-L74)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
protected function createDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function createDirectoryJailed($directory) {
    if (!ftp_mkdir($this->connection, $directory)) {
      throw new FileTransferException("Cannot create directory @directory", NULL, array("@directory" => $directory));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
