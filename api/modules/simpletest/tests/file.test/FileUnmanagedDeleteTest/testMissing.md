# FileUnmanagedDeleteTest::testMissing()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1428–1431 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1428-L1431)
- **Class:** [FileUnmanagedDeleteTest](../FileUnmanagedDeleteTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testMissing()
```

## Documentation

```text
Try deleting a missing file.
```

## Code

```php
  function testMissing() {
    // Try to delete a non-existing file
    $this->assertTrue(file_unmanaged_delete(file_default_scheme() . '/' . $this->randomName()), 'Returns true when deleting a non-existent file.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
