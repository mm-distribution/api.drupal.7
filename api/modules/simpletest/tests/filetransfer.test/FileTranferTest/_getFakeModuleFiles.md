# FileTranferTest::_getFakeModuleFiles()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 24–36 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L24-L36)
- **Class:** [FileTranferTest](../FileTranferTest.md)
- **Module/theme:** batch_test

## Signature

```php
function _getFakeModuleFiles()
```

## Documentation

_No docblock in source._

## Code

```php
  function _getFakeModuleFiles() {
    $files = array(
      'fake.module',
      'fake.info',
      'theme' => array(
        'fake.tpl.php'
      ),
      'inc' => array(
        'fake.inc'
      )
    );
    return $files;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
