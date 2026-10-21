# FileTransferLocal::isFile()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 60–62 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L60-L62)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
public function isFile($path)
```

## Documentation

_No docblock in source._

## Code

```php
  public function isFile($path) {
    return is_file($path);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
