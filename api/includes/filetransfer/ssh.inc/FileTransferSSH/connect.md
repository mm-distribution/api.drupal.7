# FileTransferSSH::connect()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 16–24 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L16-L24)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
function connect()
```

## Documentation

_No docblock in source._

## Code

```php
  function connect() {
    $this->connection = @ssh2_connect($this->hostname, $this->port);
    if (!$this->connection) {
      throw new FileTransferException('SSH Connection failed to @host:@port', NULL, array('@host' => $this->hostname, '@port' => $this->port));
    }
    if (!@ssh2_auth_password($this->connection, $this->username, $this->password)) {
      throw new FileTransferException('The supplied username/password combination was not accepted.');
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
