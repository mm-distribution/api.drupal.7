# FileUnmanagedMoveTest::testMissing()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1600–1604 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1600-L1604)
- **Class:** [FileUnmanagedMoveTest](../FileUnmanagedMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMissing()
```

## Documentation

```text
Try to move a missing file.
```

## Code

```php
  function testMissing() {
    // Move non-existent file.
    $new_filepath = file_unmanaged_move($this->randomName(), $this->randomName());
    $this->assertFalse($new_filepath, 'Moving a missing file fails.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
