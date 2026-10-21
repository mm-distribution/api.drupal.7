# FileMoveTest::testExistingRename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1846–1876 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1846-L1876)
- **Class:** [FileMoveTest](../FileMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingRename()
```

## Documentation

```text
Test renaming when moving onto a file that already exists.
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
    $result = file_move(clone $source, $target->uri, FILE_EXISTS_RENAME);

    // Check the return status and that the contents changed.
    $this->assertTrue($result, 'File moved successfully.');
    $this->assertFalse(file_exists($source->uri));
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of file correctly written.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('move', 'load', 'update'));

    // Compare the returned value to what made it into the database.
    $this->assertFileUnchanged($result, file_load($result->fid, TRUE));
    // The target file should not have been altered.
    $this->assertFileUnchanged($target, file_load($target->fid, TRUE));
    // Make sure we end up with two distinct files afterwards.
    $this->assertDifferentFile($target, $result);

    // Compare the source and results.
    $loaded_source = file_load($source->fid, TRUE);
    $this->assertEqual($loaded_source->fid, $result->fid, "Returned file's id matches the source.");
    $this->assertNotEqual($loaded_source->uri, $source->uri, 'Returned file path has changed from the original.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
