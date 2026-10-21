# FileUnmanagedCopyTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1646–1652 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1646-L1652)
- **Class:** [FileUnmanagedCopyTest](../FileUnmanagedCopyTest.md)
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
      'name' => 'Unmanaged file copying',
      'description' => 'Tests the unmanaged file copy function.',
      'group' => 'File API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
