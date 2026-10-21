# MockTestConnection::flushCommands()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 164–168 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L164-L168)
- **Class:** [MockTestConnection](../MockTestConnection.md)
- **Module/theme:** batch_test

## Signature

```php
function flushCommands()
```

## Documentation

_No docblock in source._

## Code

```php
  function flushCommands() {
    $out = $this->commandsRun;
    $this->commandsRun = array();
    return $out;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
