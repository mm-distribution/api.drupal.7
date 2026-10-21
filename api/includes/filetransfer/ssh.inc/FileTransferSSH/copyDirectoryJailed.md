# FileTransferSSH::copyDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 40–44 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L40-L44)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
protected function copyDirectoryJailed($source, $destination)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function copyDirectoryJailed($source, $destination) {
    if (@!ssh2_exec($this->connection, 'cp -Rp ' . escapeshellarg($source) . ' ' . escapeshellarg($destination))) {
      throw new FileTransferException('Cannot copy directory @directory.', NULL, array('@directory' => $source));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
