# FileUnmanagedCopyTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1657–1682 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1657-L1682)
- **Class:** [FileUnmanagedCopyTest](../FileUnmanagedCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNormal()
```

## Documentation

```text
Copy a normal file.
```

## Code

```php
  function testNormal() {
    // Create a file for testing
    $file = $this->createFile();

    // Copying to a new name.
    $desired_filepath = 'public://' . $this->randomName();
    $new_filepath = file_unmanaged_copy($file->uri, $desired_filepath, FILE_EXISTS_ERROR);
    $this->assertTrue($new_filepath, 'Copy was successful.');
    $this->assertEqual($new_filepath, $desired_filepath, 'Returned expected filepath.');
    $this->assertTrue(file_exists($file->uri), 'Original file remains.');
    $this->assertTrue(file_exists($new_filepath), 'New file exists.');
    $this->assertFilePermissions($new_filepath, variable_get('file_chmod_file', 0664));

    // Copying with rename.
    $desired_filepath = 'public://' . $this->randomName();
    $this->assertTrue(file_put_contents($desired_filepath, ' '), 'Created a file so a rename will have to happen.');
    $newer_filepath = file_unmanaged_copy($file->uri, $desired_filepath, FILE_EXISTS_RENAME);
    $this->assertTrue($newer_filepath, 'Copy was successful.');
    $this->assertNotEqual($newer_filepath, $desired_filepath, 'Returned expected filepath.');
    $this->assertTrue(file_exists($file->uri), 'Original file remains.');
    $this->assertTrue(file_exists($newer_filepath), 'New file exists.');
    $this->assertFilePermissions($newer_filepath, variable_get('file_chmod_file', 0664));

    // TODO: test copying to a directory (rather than full directory/file path)
    // TODO: test copying normal files using normal paths (rather than only streams)
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
