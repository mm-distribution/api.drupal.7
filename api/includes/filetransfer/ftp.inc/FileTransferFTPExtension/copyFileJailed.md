# FileTransferFTPExtension::copyFileJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 64–68 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L64-L68)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
protected function copyFileJailed($source, $destination)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function copyFileJailed($source, $destination) {
    if (!@ftp_put($this->connection,  $destination, $source, FTP_BINARY)) {
      throw new FileTransferException("Cannot move @source to @destination", NULL, array("@source" => $source, "@destination" => $destination));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
