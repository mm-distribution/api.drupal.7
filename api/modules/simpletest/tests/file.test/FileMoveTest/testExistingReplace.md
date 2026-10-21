# FileMoveTest::testExistingReplace()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1881–1908 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1881-L1908)
- **Class:** [FileMoveTest](../FileMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingReplace()
```

## Documentation

```text
Test replacement when moving onto a file that already exists.
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
    $result = file_move(clone $source, $target->uri, FILE_EXISTS_REPLACE);

    // Look at the results.
    $this->assertEqual($contents, file_get_contents($result->uri), 'Contents of file were overwritten.');
    $this->assertFalse(file_exists($source->uri));
    $this->assertTrue($result, 'File moved successfully.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('move', 'update', 'delete', 'load'));

    // Reload the file from the database and check that the changes were
    // actually saved.
    $loaded_result = file_load($result->fid, TRUE);
    $this->assertFileUnchanged($result, $loaded_result);
    // Check that target was re-used.
    $this->assertSameFile($target, $loaded_result);
    // Source and result should be totally different.
    $this->assertDifferentFile($source, $loaded_result);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
