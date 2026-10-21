# FileUnmanagedDeleteRecursiveTest::testEmptyDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1490–1497 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1490-L1497)
- **Class:** [FileUnmanagedDeleteRecursiveTest](../FileUnmanagedDeleteRecursiveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testEmptyDirectory()
```

## Documentation

```text
Try deleting an empty directory.
```

## Code

```php
  function testEmptyDirectory() {
    // A directory to operate on.
    $directory = $this->createDirectory();

    // Delete the directory.
    $this->assertTrue(file_unmanaged_delete_recursive($directory), 'Function reported success.');
    $this->assertFalse(file_exists($directory), 'Directory has been deleted.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
