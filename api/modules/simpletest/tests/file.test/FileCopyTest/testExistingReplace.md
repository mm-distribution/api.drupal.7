# FileCopyTest::testExistingReplace()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2046–2079 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2046-L2079)
- **Class:** [FileCopyTest](../FileCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingReplace()
```

## Documentation

```text
Test replacement when copying over a file that already exists.
```

## Code

```php
  function testExistingReplace() {
    // Setup a file to overwrite.
    $contents = $this->randomName(10);
    $source = $this->createFile(NULL, $contents);
    $target = $this->createFile();
    $this->assertDifferentFile($source, $target);

    // Clone the object so we don't have to worry about the function changing
    // our reference copy.
    $result = file_copy(clone $source, $target->uri, FILE_EXISTS_REPLACE);

    // Check the return status and that the contents changed.
    $this->assertTrue($result, 'File copied successfully.');
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of file were overwritten.');
    $this->assertDifferentFile($source, $result);

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('load', 'copy', 'update'));

    // Load all the affected files to check the changes that actually made it
    // to the database.
    $loaded_source = file_load($source->fid, TRUE);
    $loaded_target = file_load($target->fid, TRUE);
    $loaded_result = file_load($result->fid, TRUE);

    // Verify that the source file wasn't changed.
    $this->assertFileUnchanged($source, $loaded_source);

    // Verify that what was returned is what's in the database.
    $this->assertFileUnchanged($result, $loaded_result);

    // Target file was reused for the result.
    $this->assertFileUnchanged($loaded_target, $loaded_result);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
