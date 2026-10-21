# FileMoveTest::testExistingError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1936–1958 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1936-L1958)
- **Class:** [FileMoveTest](../FileMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingError()
```

## Documentation

```text
Test that moving onto an existing file fails when FILE_EXISTS_ERROR is
specified.
```

## Code

```php
  function testExistingError() {
    $contents = $this->randomName(10);
    $source = $this->createFile();
    $target = $this->createFile(NULL, $contents);
    $this->assertDifferentFile($source, $target);

    // Clone the object so we don't have to worry about the function changing
    // our reference copy.
    $result = file_move(clone $source, $target->uri, FILE_EXISTS_ERROR);

    // Check the return status and that the contents did not change.
    $this->assertFalse($result, 'File move failed.');
    $this->assertTrue(file_exists($source->uri));
    $this->assertEqual($contents, file_get_contents($target->uri), 'Contents of file were not altered.');

    // Check that no hooks were called while failing.
    $this->assertFileHooksCalled(array());

    // Load the file from the database and make sure it is identical to what
    // was returned.
    $this->assertFileUnchanged($source, file_load($source->fid, TRUE));
    $this->assertFileUnchanged($target, file_load($target->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
