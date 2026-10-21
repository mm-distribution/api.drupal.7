# TestFileTransfer::__construct()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 106–108 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L106-L108)
- **Class:** [TestFileTransfer](../TestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
function __construct($jail, $username, $password, $hostname = 'localhost', $port = 9999)
```

## Documentation

_No docblock in source._

## Code

```php
  function __construct($jail, $username, $password, $hostname = 'localhost', $port = 9999) {
    parent::__construct($jail, $username, $password, $hostname, $port);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
