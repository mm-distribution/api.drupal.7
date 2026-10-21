# TestFileTransfer::removeFileJailed()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 133–137 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L133-L137)
- **Class:** [TestFileTransfer](../TestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
function removeFileJailed($destination)
```

## Documentation

_No docblock in source._

## Code

```php
  function removeFileJailed($destination) {
    if (!ftp_delete($this->connection, $item)) {
      throw new FileTransferException('Unable to remove to file @file.', NULL, array('@file' => $item));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
