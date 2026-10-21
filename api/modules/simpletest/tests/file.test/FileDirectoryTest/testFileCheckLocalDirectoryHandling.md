# FileDirectoryTest::testFileCheckLocalDirectoryHandling()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1080–1108 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1080-L1108)
- **Class:** [FileDirectoryTest](../FileDirectoryTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileCheckLocalDirectoryHandling()
```

## Documentation

```text
Test local directory handling functions.
```

## Code

```php
  function testFileCheckLocalDirectoryHandling() {
    $directory = file_default_scheme() . '://';

    // Check a new recursively created local directory for correct file system
    // permissions.
    $parent = $this->randomName();
    $child = $this->randomName();

    // Files directory already exists.
    $this->assertTrue(is_dir($directory), 'Files directory already exists.', 'File');
    // Make files directory writable only.
    $old_mode = fileperms($directory);

    // Create the directories.
    $parent_path = $directory . DIRECTORY_SEPARATOR . $parent;
    $child_path = $parent_path . DIRECTORY_SEPARATOR . $child;
    $this->assertTrue(drupal_mkdir($child_path, 0775, TRUE), 'No error reported when creating new local directories.', 'File');

    // Ensure new directories also exist.
    $this->assertTrue(is_dir($parent_path), 'New parent directory actually exists.', 'File');
    $this->assertTrue(is_dir($child_path), 'New child directory actually exists.', 'File');

    // Check that new directory permissions were set properly.
    $this->assertDirectoryPermissions($parent_path, 0775);
    $this->assertDirectoryPermissions($child_path, 0775);

    // Check that existing directory permissions were not modified.
    $this->assertDirectoryPermissions($directory, $old_mode);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
