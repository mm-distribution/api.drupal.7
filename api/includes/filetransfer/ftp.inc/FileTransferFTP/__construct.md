# FileTransferFTP::__construct()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 8–14 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L8-L14)
- **Class:** [FileTransferFTP](../FileTransferFTP.md)

## Signature

```php
public function __construct($jail, $username, $password, $hostname, $port)
```

## Documentation

_No docblock in source._

## Code

```php
  public function __construct($jail, $username, $password, $hostname, $port) {
    $this->username = $username;
    $this->password = $password;
    $this->hostname = $hostname;
    $this->port = $port;
    parent::__construct($jail);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
