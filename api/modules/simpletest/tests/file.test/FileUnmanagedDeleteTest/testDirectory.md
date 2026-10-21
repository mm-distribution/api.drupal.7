# FileUnmanagedDeleteTest::testDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1436–1443 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1436-L1443)
- **Class:** [FileUnmanagedDeleteTest](../FileUnmanagedDeleteTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDirectory()
```

## Documentation

```text
Try deleting a directory.
```

## Code

```php
  function testDirectory() {
    // A directory to operate on.
    $directory = $this->createDirectory();

    // Try to delete a directory
    $this->assertFalse(file_unmanaged_delete($directory), 'Could not delete the delete directory.');
    $this->assertTrue(file_exists($directory), 'Directory has not been deleted.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
