# FileTransferSSH

- **Type:** Class
- **File:** [`includes/filetransfer/ssh.inc`](_file.md), lines 6–110 · [local source](../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L6-L110)

## Signature

```php
class FileTransferSSH extends FileTransfer implements FileTransferChmodInterface
```

## Documentation

```text
The SSH connection class for the update module.
```

## Methods (derived index)

- [__construct()](FileTransferSSH/__construct.md)
- [connect()](FileTransferSSH/connect.md)
- [factory()](FileTransferSSH/factory.md)
- [copyFileJailed()](FileTransferSSH/copyFileJailed.md)
- [copyDirectoryJailed()](FileTransferSSH/copyDirectoryJailed.md)
- [createDirectoryJailed()](FileTransferSSH/createDirectoryJailed.md)
- [removeDirectoryJailed()](FileTransferSSH/removeDirectoryJailed.md)
- [removeFileJailed()](FileTransferSSH/removeFileJailed.md)
- [isDirectory()](FileTransferSSH/isDirectory.md) — WARNING: This is untested.  It is not currently used, but should do the trick.
- [isFile()](FileTransferSSH/isFile.md)
- [chmodJailed()](FileTransferSSH/chmodJailed.md)
- [getSettingsForm()](FileTransferSSH/getSettingsForm.md) — Returns the form to configure the FileTransfer class for SSH.

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
