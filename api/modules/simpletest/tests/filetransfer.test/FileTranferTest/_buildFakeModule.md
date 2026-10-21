# FileTranferTest::_buildFakeModule()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 38–52 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L38-L52)
- **Class:** [FileTranferTest](../FileTranferTest.md)
- **Module/theme:** batch_test

## Signature

```php
function _buildFakeModule()
```

## Documentation

_No docblock in source._

## Code

```php
  function _buildFakeModule() {
    $location = 'temporary://fake';
    if (is_dir($location)) {
      $ret = 0;
      $output = array();
      exec('rm -Rf ' . escapeshellarg($location), $output, $ret);
      if ($ret != 0) {
        throw new Exception('Error removing fake module directory.');
      }
    }

    $files = $this->_getFakeModuleFiles();
    $this->_writeDirectory($location, $files);
    return $location;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
