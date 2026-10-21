# FileUnmanagedDeleteTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1416–1423 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1416-L1423)
- **Class:** [FileUnmanagedDeleteTest](../FileUnmanagedDeleteTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNormal()
```

## Documentation

```text
Delete a normal file.
```

## Code

```php
  function testNormal() {
    // Create a file for testing
    $file = $this->createFile();

    // Delete a regular file
    $this->assertTrue(file_unmanaged_delete($file->uri), 'Deleted worked.');
    $this->assertFalse(file_exists($file->uri), 'Test file has actually been deleted.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
