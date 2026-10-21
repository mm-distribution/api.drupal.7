# FileUnmanagedMoveTest::testOverwriteSelf()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1609–1623 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1609-L1623)
- **Class:** [FileUnmanagedMoveTest](../FileUnmanagedMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOverwriteSelf()
```

## Documentation

```text
Try to move a file onto itself.
```

## Code

```php
  function testOverwriteSelf() {
    // Create a file for testing.
    $file = $this->createFile();

    // Move the file onto itself without renaming shouldn't make changes.
    $new_filepath = file_unmanaged_move($file->uri, $file->uri, FILE_EXISTS_REPLACE);
    $this->assertFalse($new_filepath, 'Moving onto itself without renaming fails.');
    $this->assertTrue(file_exists($file->uri), 'File exists after moving onto itself.');

    // Move the file onto itself with renaming will result in a new filename.
    $new_filepath = file_unmanaged_move($file->uri, $file->uri, FILE_EXISTS_RENAME);
    $this->assertTrue($new_filepath, 'Moving onto itself with renaming works.');
    $this->assertFalse(file_exists($file->uri), 'Original file has been removed.');
    $this->assertTrue(file_exists($new_filepath), 'File exists after moving onto itself.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
