# FileCopyTest::testExistingRename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2006–2041 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2006-L2041)
- **Class:** [FileCopyTest](../FileCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingRename()
```

## Documentation

```text
Test renaming when copying over a file that already exists.
```

## Code

```php
  function testExistingRename() {
    // Setup a file to overwrite.
    $contents = $this->randomName(10);
    $source = $this->createFile(NULL, $contents);
    $target = $this->createFile();
    $this->assertDifferentFile($source, $target);

    // Clone the object so we don't have to worry about the function changing
    // our reference copy.
    $result = file_copy(clone $source, $target->uri, FILE_EXISTS_RENAME);

    // Check the return status and that the contents changed.
    $this->assertTrue($result, 'File copied successfully.');
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of file were copied correctly.');
    $this->assertNotEqual($result->uri, $source->uri, 'Returned file path has changed from the original.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('copy', 'insert'));

    // Load all the affected files to check the changes that actually made it
    // to the database.
    $loaded_source = file_load($source->fid, TRUE);
    $loaded_target = file_load($target->fid, TRUE);
    $loaded_result = file_load($result->fid, TRUE);

    // Verify that the source file wasn't changed.
    $this->assertFileUnchanged($source, $loaded_source);

    // Verify that what was returned is what's in the database.
    $this->assertFileUnchanged($result, $loaded_result);

    // Make sure we end up with three distinct files afterwards.
    $this->assertDifferentFile($loaded_source, $loaded_target);
    $this->assertDifferentFile($loaded_target, $loaded_result);
    $this->assertDifferentFile($loaded_source, $loaded_result);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
