# includes/updater.inc

- **Source:** [local](../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · 435 lines

## File documentation

```text
@file
Classes used for updating various files in the Drupal webroot. These
classes use a FileTransfer object to actually perform the operations.
Normally, the FileTransfer is provided when the site owner is redirected to
authorize.php as part of a multistep process.
```

## Classes and interfaces (derived index)

- [DrupalUpdaterInterface](DrupalUpdaterInterface.md) — Interface for a class which can update a Drupal project.
- [Updater](Updater.md) — Base class for Updaters used in Drupal.
- [UpdaterException](UpdaterException.md) — Exception class for the Updater class hierarchy.
- [UpdaterFileTransferException](UpdaterFileTransferException.md) — Child class of UpdaterException that indicates a FileTransfer exception.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
