# FileTransferLocal::factory()

- **Type:** Method
- **File:** [`includes/filetransfer/local.inc`](../_file.md), lines 12–14 · [local source](../../../../../source/includes/filetransfer/local.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc#L12-L14)
- **Class:** [FileTransferLocal](../FileTransferLocal.md)

## Signature

```php
static function factory($jail, $settings)
```

## Documentation

_No docblock in source._

## Code

```php
  static function factory($jail, $settings) {
    return new FileTransferLocal($jail);
  }
```

---
_Drupal 7.103 · [includes/filetransfer/local.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/local.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
