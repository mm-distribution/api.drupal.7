# FileUnmanagedDeleteRecursiveTest::testDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1502–1515 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1502-L1515)
- **Class:** [FileUnmanagedDeleteRecursiveTest](../FileUnmanagedDeleteRecursiveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDirectory()
```

## Documentation

```text
Try deleting a directory with some files.
```

## Code

```php
  function testDirectory() {
    // A directory to operate on.
    $directory = $this->createDirectory();
    $filepathA = $directory . '/A';
    $filepathB = $directory . '/B';
    file_put_contents($filepathA, '');
    file_put_contents($filepathB, '');

    // Delete the directory.
    $this->assertTrue(file_unmanaged_delete_recursive($directory), 'Function reported success.');
    $this->assertFalse(file_exists($filepathA), 'Test file A has been deleted.');
    $this->assertFalse(file_exists($filepathB), 'Test file B has been deleted.');
    $this->assertFalse(file_exists($directory), 'Directory has been deleted.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
