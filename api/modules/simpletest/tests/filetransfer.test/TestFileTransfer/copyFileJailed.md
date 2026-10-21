# TestFileTransfer::copyFileJailed()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 121–123 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L121-L123)
- **Class:** [TestFileTransfer](../TestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
function copyFileJailed($source, $destination)
```

## Documentation

_No docblock in source._

## Code

```php
  function copyFileJailed($source, $destination) {
    $this->connection->run("copyFile $source $destination");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
