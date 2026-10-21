# FileDeleteTest::testUnused()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1761–1770 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1761-L1770)
- **Class:** [FileDeleteTest](../FileDeleteTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testUnused()
```

## Documentation

```text
Tries deleting a normal file (as opposed to a directory, symlink, etc).
```

## Code

```php
  function testUnused() {
    $file = $this->createFile();

    // Check that deletion removes the file and database record.
    $this->assertTrue(is_file($file->uri), 'File exists.');
    $this->assertIdentical(file_delete($file), TRUE, 'Delete worked.');
    $this->assertFileHooksCalled(array('delete'));
    $this->assertFalse(file_exists($file->uri), 'Test file has actually been deleted.');
    $this->assertFalse(file_load($file->fid), 'File was removed from the database.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
