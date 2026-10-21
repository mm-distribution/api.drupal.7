# SkipDotsRecursiveDirectoryIterator

- **Type:** Class
- **File:** [`includes/filetransfer/filetransfer.inc`](_file.md), lines 402–431 · [local source](../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L402-L431)

## Signature

```php
class SkipDotsRecursiveDirectoryIterator extends RecursiveDirectoryIterator
```

## Documentation

```text
Provides an interface for iterating recursively over filesystem directories.

Manually skips '.' and '..' directories, since no existing method is
available in PHP 5.2.

@todo Depreciate in favor of RecursiveDirectoryIterator::SKIP_DOTS once PHP
  5.3 or later is required.
```

## Methods (derived index)

- [__construct()](SkipDotsRecursiveDirectoryIterator/__construct.md) — Constructs a SkipDotsRecursiveDirectoryIterator
- [rewind()](SkipDotsRecursiveDirectoryIterator/rewind.md)
- [next()](SkipDotsRecursiveDirectoryIterator/next.md)
- [skipdots()](SkipDotsRecursiveDirectoryIterator/skipdots.md)

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
