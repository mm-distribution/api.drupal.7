# FileTransferSSH::copyFileJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 34–38 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L34-L38)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
protected function copyFileJailed($source, $destination)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function copyFileJailed($source, $destination) {
    if (!@ssh2_scp_send($this->connection, $source, $destination)) {
      throw new FileTransferException('Cannot copy @source_file to @destination_file.', NULL, array('@source' => $source, '@destination' => $destination));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
