# FileTransferLocal::isDirectory()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 56–58 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L56-L58)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
public function isDirectory($path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isDirectory($path) {
    return is_dir($path);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
