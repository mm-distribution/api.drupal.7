# FileTransferLocal::createDirectoryJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 22–26 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L22-L26)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
protected function createDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function createDirectoryJailed($directory) {
    if (!is_dir($directory) && @!mkdir($directory, 0777, TRUE)) {
      throw new FileTransferException('Cannot create directory %directory.', NULL, array('%directory' => $directory));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
