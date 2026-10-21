# FileUnmanagedCopyTest::testOverwriteSelf()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1698–1727 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1698-L1727)
- **Class:** [FileUnmanagedCopyTest](../FileUnmanagedCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testOverwriteSelf()
```

## Documentation

```text
Copy a file onto itself.
```

## Code

```php
  function testOverwriteSelf() {
    // Create a file for testing
    $file = $this->createFile();

    // Copy the file onto itself with renaming works.
    $new_filepath = file_unmanaged_copy($file->uri, $file->uri, FILE_EXISTS_RENAME);
    $this->assertTrue($new_filepath, 'Copying onto itself with renaming works.');
    $this->assertNotEqual($new_filepath, $file->uri, 'Copied file has a new name.');
    $this->assertTrue(file_exists($file->uri), 'Original file exists after copying onto itself.');
    $this->assertTrue(file_exists($new_filepath), 'Copied file exists after copying onto itself.');
    $this->assertFilePermissions($new_filepath, variable_get('file_chmod_file', 0664));

    // Copy the file onto itself without renaming fails.
    $new_filepath = file_unmanaged_copy($file->uri, $file->uri, FILE_EXISTS_ERROR);
    $this->assertFalse($new_filepath, 'Copying onto itself without renaming fails.');
    $this->assertTrue(file_exists($file->uri), 'File exists after copying onto itself.');

    // Copy the file into same directory without renaming fails.
    $new_filepath = file_unmanaged_copy($file->uri, drupal_dirname($file->uri), FILE_EXISTS_ERROR);
    $this->assertFalse($new_filepath, 'Copying onto itself fails.');
    $this->assertTrue(file_exists($file->uri), 'File exists after copying onto itself.');

    // Copy the file into same directory with renaming works.
    $new_filepath = file_unmanaged_copy($file->uri, drupal_dirname($file->uri), FILE_EXISTS_RENAME);
    $this->assertTrue($new_filepath, 'Copying into same directory works.');
    $this->assertNotEqual($new_filepath, $file->uri, 'Copied file has a new name.');
    $this->assertTrue(file_exists($file->uri), 'Original file exists after copying onto itself.');
    $this->assertTrue(file_exists($new_filepath), 'Copied file exists after copying onto itself.');
    $this->assertFilePermissions($new_filepath, variable_get('file_chmod_file', 0664));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
