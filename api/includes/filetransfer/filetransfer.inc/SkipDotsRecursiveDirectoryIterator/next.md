# SkipDotsRecursiveDirectoryIterator::next()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 421–424 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L421-L424)
- **Class:** [SkipDotsRecursiveDirectoryIterator](../SkipDotsRecursiveDirectoryIterator.md)

## Signature

```php
function next()
```

## Documentation

_No docblock in source._

## Code

```php
  function next() {
    parent::next();
    $this->skipdots();
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
