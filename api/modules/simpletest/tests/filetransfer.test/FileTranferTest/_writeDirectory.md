# FileTranferTest::_writeDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 54–65 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L54-L65)
- **Class:** [FileTranferTest](../FileTranferTest.md)
- **Module/theme:** batch_test

## Signature

```php
function _writeDirectory($base, $files = array())
```

## Documentation

_No docblock in source._

## Code

```php
  function _writeDirectory($base, $files = array()) {
    mkdir($base);
    foreach ($files as $key => $file) {
      if (is_array($file)) {
        $this->_writeDirectory($base . DIRECTORY_SEPARATOR . $key, $file);
      }
      else {
        //just write the filename into the file
        file_put_contents($base . DIRECTORY_SEPARATOR . $file, $file);
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
