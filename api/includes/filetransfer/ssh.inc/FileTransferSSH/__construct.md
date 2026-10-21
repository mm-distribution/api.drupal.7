# FileTransferSSH::__construct()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 8–14 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L8-L14)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
function __construct($jail, $username, $password, $hostname = "localhost", $port = 22)
```

## Documentation

_No docblock in source._

## Code

```php
  function __construct($jail, $username, $password, $hostname = "localhost", $port = 22) {
    $this->username = $username;
    $this->password = $password;
    $this->hostname = $hostname;
    $this->port = $port;
    parent::__construct($jail);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
