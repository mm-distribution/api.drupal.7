# FileTranferTest::testJail()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 67–89 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L67-L89)
- **Class:** [FileTranferTest](../FileTranferTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testJail()
```

## Documentation

_No docblock in source._

## Code

```php
  function testJail() {
    $source = $this->_buildFakeModule();

    // This convoluted piece of code is here because our testing framework does
    // not support expecting exceptions.
    $gotit = FALSE;
    try {
      $this->testConnection->copyDirectory($source, '/tmp');
    }
    catch (FileTransferException $e) {
      $gotit = TRUE;
    }
    $this->assertTrue($gotit, 'Was not able to copy a directory outside of the jailed area.');

    $gotit = TRUE;
    try {
      $this->testConnection->copyDirectory($source, DRUPAL_ROOT . '/'. variable_get('file_public_path', conf_path() . '/files'));
    }
    catch (FileTransferException $e) {
      $gotit = FALSE;
    }
    $this->assertTrue($gotit, 'Was able to copy a directory inside of the jailed area');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
