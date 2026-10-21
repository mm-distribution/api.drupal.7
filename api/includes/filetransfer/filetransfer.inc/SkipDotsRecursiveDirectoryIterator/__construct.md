# SkipDotsRecursiveDirectoryIterator::__construct()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 409–412 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L409-L412)
- **Class:** [SkipDotsRecursiveDirectoryIterator](../SkipDotsRecursiveDirectoryIterator.md)

## Signature

```php
function __construct($path)
```

## Documentation

```text
Constructs a SkipDotsRecursiveDirectoryIterator

@param $path
  The path of the directory to be iterated over.
```

## Code

```php
  function __construct($path) {
    parent::__construct($path);
    $this->skipdots();
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
