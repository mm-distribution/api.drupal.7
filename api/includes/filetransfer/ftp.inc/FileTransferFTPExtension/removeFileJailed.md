# FileTransferFTPExtension::removeFileJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 103–107 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L103-L107)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
protected function removeFileJailed($destination)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function removeFileJailed($destination) {
    if (!ftp_delete($this->connection, $destination)) {
      throw new FileTransferException("Unable to remove to file @file", NULL, array('@file' => $destination));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
