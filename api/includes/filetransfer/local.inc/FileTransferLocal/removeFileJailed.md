# FileTransferLocal::removeFileJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 50–54 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L50-L54)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
protected function removeFileJailed($file)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function removeFileJailed($file) {
    if (@!drupal_unlink($file)) {
      throw new FileTransferException('Cannot remove file %file.', NULL, array('%file' => $file));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
