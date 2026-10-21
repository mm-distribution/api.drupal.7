# SkipDotsRecursiveDirectoryIterator::rewind()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 415–418 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L415-L418)
- **Class:** [SkipDotsRecursiveDirectoryIterator](../SkipDotsRecursiveDirectoryIterator.md)

## Signature

```php
function rewind()
```

## Documentation

_No docblock in source._

## Code

```php
  function rewind() {
    parent::rewind();
    $this->skipdots();
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
