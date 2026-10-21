# FileTransferSSH::removeDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 52–56 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L52-L56)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
protected function removeDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function removeDirectoryJailed($directory) {
    if (@!ssh2_exec($this->connection, 'rm -Rf ' . escapeshellarg($directory))) {
      throw new FileTransferException('Cannot remove @directory.', NULL, array('@directory' => $directory));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
