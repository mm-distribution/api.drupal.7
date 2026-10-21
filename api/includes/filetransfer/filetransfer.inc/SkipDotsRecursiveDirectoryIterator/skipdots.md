# SkipDotsRecursiveDirectoryIterator::skipdots()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 426–430 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L426-L430)
- **Class:** [SkipDotsRecursiveDirectoryIterator](../SkipDotsRecursiveDirectoryIterator.md)

## Signature

```php
protected function skipdots()
```

## Documentation

_No docblock in source._

## Code

```php
  protected function skipdots() {
    while ($this->isDot()) {
      parent::next();
    }
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
