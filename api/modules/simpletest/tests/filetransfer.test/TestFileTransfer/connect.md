# TestFileTransfer::connect()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 114–119 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L114-L119)
- **Class:** [TestFileTransfer](../TestFileTransfer.md)
- **Module/theme:** batch_test

## Signature

```php
function connect()
```

## Documentation

_No docblock in source._

## Code

```php
  function connect() {
    $parts = explode(':', $this->hostname);
    $port = (count($parts) == 2) ? $parts[1] : $this->port;
    $this->connection = new MockTestConnection();
    $this->connection->connectionString = 'test://' . urlencode((string) $this->username) . ':' . urlencode((string) $this->password) . "@$this->host:$this->port/";
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
