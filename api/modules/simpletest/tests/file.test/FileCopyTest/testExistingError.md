# FileCopyTest::testExistingError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2085–2104 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2085-L2104)
- **Class:** [FileCopyTest](../FileCopyTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingError()
```

## Documentation

```text
Test that copying over an existing file fails when FILE_EXISTS_ERROR is
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
    $result = file_copy(clone $source, $target->uri, FILE_EXISTS_ERROR);

    // Check the return status and that the contents were not changed.
    $this->assertFalse($result, 'File copy failed.');
    $this->assertEqual($contents, file_get_contents($target->uri), 'Contents of file were not altered.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array());

    $this->assertFileUnchanged($source, file_load($source->fid, TRUE));
    $this->assertFileUnchanged($target, file_load($target->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
