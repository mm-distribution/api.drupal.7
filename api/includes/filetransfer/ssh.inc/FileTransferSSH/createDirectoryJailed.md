# FileTransferSSH::createDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 46–50 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L46-L50)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
protected function createDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function createDirectoryJailed($directory) {
    if (@!ssh2_exec($this->connection, 'mkdir ' . escapeshellarg($directory))) {
      throw new FileTransferException('Cannot create directory @directory.', NULL, array('@directory' => $directory));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
