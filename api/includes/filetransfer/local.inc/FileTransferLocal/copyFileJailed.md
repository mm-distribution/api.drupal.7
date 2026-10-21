# FileTransferLocal::copyFileJailed()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 16–20 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L16-L20)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
protected function copyFileJailed($source, $destination)
```

## Documentation

_No docblock in source._

## Code

```php
  protected function copyFileJailed($source, $destination) {
    if (@!copy($source, $destination)) {
      throw new FileTransferException('Cannot copy %source to %destination.', NULL, array('%source' => $source, '%destination' => $destination));
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
