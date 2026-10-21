# UpdaterFileTransferException

- **Type:** Class
- **File:** [`includes/updater.inc`](_file.md), lines 433–434 · [local source](../../../source/includes/updater.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc#L433-L434)

## Signature

```php
class UpdaterFileTransferException extends UpdaterException
```

## Documentation

```text
Child class of UpdaterException that indicates a FileTransfer exception.

We have to catch FileTransfer exceptions and wrap those in t(), since
FileTransfer is so low-level that it doesn't use any Drupal APIs and none
of the strings are translated.
```

---
_Drupal 7.103 · [includes/updater.inc](https://github.com/drupal/drupal/blob/7.103/includes/updater.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
