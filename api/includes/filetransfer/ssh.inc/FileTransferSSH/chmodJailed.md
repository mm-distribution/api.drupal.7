# FileTransferSSH::chmodJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 95–100 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L95-L100)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
function chmodJailed($path, $mode, $recursive)
```

## Documentation

_No docblock in source._

## Code

```php
  function chmodJailed($path, $mode, $recursive) {
    $cmd = sprintf("chmod %s%o %s", $recursive ? '-R ' : '', $mode, escapeshellarg($path));
    if (@!ssh2_exec($this->connection, $cmd)) {
      throw new FileTransferException('Cannot change permissions of @path.', NULL, array('@path' => $path));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
