# FileMoveTest::testExistingReplaceSelf()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1913–1930 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1913-L1930)
- **Class:** [FileMoveTest](../FileMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingReplaceSelf()
```

## Documentation

```text
Test replacement when moving onto itself.
```

## Code

```php
  function testExistingReplaceSelf() {
    // Setup a file to overwrite.
    $contents = $this->randomName(10);
    $source = $this->createFile(NULL, $contents);

    // Copy the file over itself. Clone the object so we don't have to worry
    // about the function changing our reference copy.
    $result = file_move(clone $source, $source->uri, FILE_EXISTS_REPLACE);
    $this->assertFalse($result, 'File move failed.');
    $this->assertEqual($contents, file_get_contents($source->uri), 'Contents of file were not altered.');

    // Check that no hooks were called while failing.
    $this->assertFileHooksCalled(array());

    // Load the file from the database and make sure it is identical to what
    // was returned.
    $this->assertFileUnchanged($source, file_load($source->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
