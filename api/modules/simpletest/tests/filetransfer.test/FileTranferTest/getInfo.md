# FileTranferTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/filetransfer.test`](../_file.md), lines 11–17 · [local source](../../../../../../source/modules/simpletest/tests/filetransfer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test#L11-L17)
- **Class:** [FileTranferTest](../FileTranferTest.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'FileTransfer unit tests',
      'description' => 'Test that the jail is respected and that protocols using recursive file move operations work.',
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/filetransfer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/filetransfer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
