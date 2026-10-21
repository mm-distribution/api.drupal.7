# MockTestConnection::run()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 160–162 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L160-L162)
- **Class:** [MockTestConnection](../MockTestConnection.md)
- **Module/theme:** batch_test

## Signature

```php
function run($cmd)
```

## Documentation

_No docblock in source._

## Code

```php
  function run($cmd) {
    $this->commandsRun[] = $cmd;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
