# FileTransferSSH::removeFileJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 58–62 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L58-L62)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
protected function removeFileJailed($destination)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function removeFileJailed($destination) {
    if (!@ssh2_exec($this->connection, 'rm ' . escapeshellarg($destination))) {
      throw new FileTransferException('Cannot remove @directory.', NULL, array('@directory' => $destination));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
