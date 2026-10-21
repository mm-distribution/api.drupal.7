# FileDirectoryTest::testFileCheckDirectoryHandling()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1113–1152 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1113-L1152)
- **Class:** [FileDirectoryTest](../FileDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileCheckDirectoryHandling()
```

## Documentation

```text
Test directory handling functions.
```

## Code

```php
  function testFileCheckDirectoryHandling() {
    // A directory to operate on.
    $directory = file_default_scheme() . '://' . $this->randomName() . '/' . $this->randomName();
    $this->assertFalse(is_dir($directory), 'Directory does not exist prior to testing.');

    // Non-existent directory.
    $this->assertFalse(file_prepare_directory($directory, 0), 'Error reported for non-existing directory.', 'File');

    // Make a directory.
    $this->assertTrue(file_prepare_directory($directory, FILE_CREATE_DIRECTORY), 'No error reported when creating a new directory.', 'File');

    // Make sure directory actually exists.
    $this->assertTrue(is_dir($directory), 'Directory actually exists.', 'File');

    if (substr(PHP_OS, 0, 3) != 'WIN') {
      // PHP on Windows doesn't support any kind of useful read-only mode for
      // directories. When executing a chmod() on a directory, PHP only sets the
      // read-only flag, which doesn't prevent files to actually be written
      // in the directory on any recent version of Windows.

      // Make directory read only.
      @drupal_chmod($directory, 0444);
      $this->assertFalse(file_prepare_directory($directory, 0), 'Error reported for a non-writeable directory.', 'File');

      // Test directory permission modification.
      $this->assertTrue(file_prepare_directory($directory, FILE_MODIFY_PERMISSIONS), 'No error reported when making directory writeable.', 'File');
    }

    // Test that the directory has the correct permissions.
    $this->assertDirectoryPermissions($directory, variable_get('file_chmod_directory', 0775));

    // Remove .htaccess file to then test that it gets re-created.
    @drupal_unlink(file_default_scheme() . '://.htaccess');
    $this->assertFalse(is_file(file_default_scheme() . '://.htaccess'), 'Successfully removed the .htaccess file in the files directory.', 'File');
    file_ensure_htaccess();
    $this->assertTrue(is_file(file_default_scheme() . '://.htaccess'), 'Successfully re-created the .htaccess file in the files directory.', 'File');
    // Verify contents of .htaccess file.
    $file = file_get_contents(file_default_scheme() . '://.htaccess');
    $this->assertEqual($file, file_htaccess_lines(FALSE), 'The .htaccess file contains the proper content.', 'File');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
