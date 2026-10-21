# FileTransfer::factory()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 42–44 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L42-L44)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
static function factory($jail, $settings)
```

## Documentation

```text
Classes that extend this class must override the factory() static method.

@param string $jail
  The full path where all file operations performed by this object will
  be restricted to. This prevents the FileTransfer classes from being
  able to touch other parts of the filesystem.
@param array $settings
  An array of connection settings for the FileTransfer subclass. If the
  getSettingsForm() method uses any nested settings, the same structure
  will be assumed here.
@return object
  New instance of the appropriate FileTransfer subclass.
```

## Code

```php
  static function factory($jail, $settings) {
    throw new FileTransferException('FileTransfer::factory() static method not overridden by FileTransfer subclass.');
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
