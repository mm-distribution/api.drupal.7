# FileTransfer

- **Type:** Class
- **File:** [`includes/filetransfer/filetransfer.inc`](_file.md), lines 13–360 · [local source](../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L13-L360)

## Signature

```php
abstract class FileTransfer
```

## Documentation

_No docblock in source._

## Properties

### $username

```php
protected $username;
```

### $password

```php
protected $password;
```

### $hostname

```php
protected $hostname = 'localhost';
```

### $port

```php
protected $port;
```

### $jail

```php
protected $jail;
```

## Methods (derived index)

- [__construct()](FileTransfer/__construct.md) — The constructor for the UpdateConnection class. This method is also called from the classes that extend this class and override this method.
- [factory()](FileTransfer/factory.md) — Classes that extend this class must override the factory() static method.
- [__get()](FileTransfer/__get.md) — Implementation of the magic __get() method.
- [connect()](FileTransfer/connect.md) — Connect to the server.
- [copyDirectory()](FileTransfer/copyDirectory.md) — Copies a directory.
- [chmod()](FileTransfer/chmod.md)
- [createDirectory()](FileTransfer/createDirectory.md) — Creates a directory.
- [removeDirectory()](FileTransfer/removeDirectory.md) — Removes a directory.
- [copyFile()](FileTransfer/copyFile.md) — Copies a file.
- [removeFile()](FileTransfer/removeFile.md) — Removes a file.
- [checkPath()](FileTransfer/checkPath.md) — Checks that the path is inside the jail and throws an exception if not.
- [fixRemotePath()](FileTransfer/fixRemotePath.md) — Returns a modified path suitable for passing to the server. If a path is a windows path, makes it POSIX compliant by removing the drive letter. If $this->chroot has a value, it is stripped from the path to allow for chroot'd filetransfer systems.
- [sanitizePath()](FileTransfer/sanitizePath.md) — Changes backslashes to slashes, also removes a trailing slash.
- [copyDirectoryJailed()](FileTransfer/copyDirectoryJailed.md) — Copies a directory.
- [createDirectoryJailed()](FileTransfer/createDirectoryJailed.md) — Creates a directory.
- [removeDirectoryJailed()](FileTransfer/removeDirectoryJailed.md) — Removes a directory.
- [copyFileJailed()](FileTransfer/copyFileJailed.md) — Copies a file.
- [removeFileJailed()](FileTransfer/removeFileJailed.md) — Removes a file.
- [isDirectory()](FileTransfer/isDirectory.md) — Checks if a particular path is a directory
- [isFile()](FileTransfer/isFile.md) — Checks if a particular path is a file (not a directory).
- [findChroot()](FileTransfer/findChroot.md) — Return the chroot property for this connection.
- [setChroot()](FileTransfer/setChroot.md) — Sets the chroot and changes the jail to match the correct path scheme
- [getSettingsForm()](FileTransfer/getSettingsForm.md) — Returns a form to collect connection settings credentials.

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
