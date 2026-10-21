# FileTransferFTPExtension::isDirectory()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 109–117 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L109-L117)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
public function isDirectory($path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isDirectory($path) {
    $result = FALSE;
    $curr = ftp_pwd($this->connection);
    if (@ftp_chdir($this->connection, $path)) {
      $result = TRUE;
    }
    ftp_chdir($this->connection, $curr);
    return $result;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
