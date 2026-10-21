# FileUnmanagedDeleteRecursiveTest::testSubDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1520–1535 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1520-L1535)
- **Class:** [FileUnmanagedDeleteRecursiveTest](../FileUnmanagedDeleteRecursiveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSubDirectory()
```

## Documentation

```text
Try deleting subdirectories with some files.
```

## Code

```php
  function testSubDirectory() {
    // A directory to operate on.
    $directory = $this->createDirectory();
    $subdirectory = $this->createDirectory($directory . '/sub');
    $filepathA = $directory . '/A';
    $filepathB = $subdirectory . '/B';
    file_put_contents($filepathA, '');
    file_put_contents($filepathB, '');

    // Delete the directory.
    $this->assertTrue(file_unmanaged_delete_recursive($directory), 'Function reported success.');
    $this->assertFalse(file_exists($filepathA), 'Test file A has been deleted.');
    $this->assertFalse(file_exists($filepathB), 'Test file B has been deleted.');
    $this->assertFalse(file_exists($subdirectory), 'Subdirectory has been deleted.');
    $this->assertFalse(file_exists($directory), 'Directory has been deleted.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
