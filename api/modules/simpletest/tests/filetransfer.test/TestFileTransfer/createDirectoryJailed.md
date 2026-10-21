# TestFileTransfer::createDirectoryJailed()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 129–131 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L129-L131)
- **Class:** [TestFileTransfer](../TestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
function createDirectoryJailed($directory)
```

## Documentation

_No docblock in source._

## Code

```php
  function createDirectoryJailed($directory) {
    $this->connection->run("mkdir $directory");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
