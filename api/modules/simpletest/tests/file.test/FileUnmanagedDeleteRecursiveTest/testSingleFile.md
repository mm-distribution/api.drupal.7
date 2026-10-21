# FileUnmanagedDeleteRecursiveTest::testSingleFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1477–1485 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1477-L1485)
- **Class:** [FileUnmanagedDeleteRecursiveTest](../FileUnmanagedDeleteRecursiveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSingleFile()
```

## Documentation

```text
Delete a normal file.
```

## Code

```php
  function testSingleFile() {
    // Create a file for testing
    $filepath = file_default_scheme() . '://' . $this->randomName();
    file_put_contents($filepath, '');

    // Delete the file.
    $this->assertTrue(file_unmanaged_delete_recursive($filepath), 'Function reported success.');
    $this->assertFalse(file_exists($filepath), 'Test file has been deleted.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
