# TestFileTransfer::isDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 139–141 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L139-L141)
- **Class:** [TestFileTransfer](../TestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
function isDirectory($path)
```

## Documentation

_No docblock in source._

## Code

```php
  function isDirectory($path) {
    return $this->shouldIsDirectoryReturnTrue;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
