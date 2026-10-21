# FileTransferFTPExtension::isFile()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 119–121 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L119-L121)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
public function isFile($path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isFile($path) {
    return ftp_size($this->connection, $path) != -1;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
