# FileUnmanagedMoveTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1558–1564 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1558-L1564)
- **Class:** [FileUnmanagedMoveTest](../FileUnmanagedMoveTest.md)
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
      'name' => 'Unmanaged file moving',
      'description' => 'Tests the unmanaged file move function.',
      'group' => 'File API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
