# FileTransferFTPExtension::connect()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 53–62 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L53-L62)
- **Class:** [FileTransferFTPExtension](../FileTransferFTPExtension.md)

## Signature

```php
public function connect()
```

## Documentation

_No docblock in source._

## Code

```php
  public function connect() {
    $this->connection = ftp_connect($this->hostname, $this->port);

    if (!$this->connection) {
      throw new FileTransferException("Cannot connect to FTP Server, check settings");
    }
    if (!ftp_login($this->connection, $this->username, $this->password)) {
      throw new FileTransferException("Cannot log in to FTP server. Check username and password");
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
