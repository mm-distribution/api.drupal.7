# FileSaveDataTest::testExistingError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 2549–2563 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L2549-L2563)
- **Class:** [FileSaveDataTest](../FileSaveDataTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingError()
```

## Documentation

```text
Test that file_save_data() fails overwriting an existing file.
```

## Code

```php
  function testExistingError() {
    $contents = $this->randomName(8);
    $existing = $this->createFile(NULL, $contents);

    // Check the overwrite error.
    $result = file_save_data('asdf', $existing->uri, FILE_EXISTS_ERROR);
    $this->assertFalse($result, 'Overwriting a file fails when FILE_EXISTS_ERROR is specified.');
    $this->assertEqual($contents, file_get_contents($existing->uri), 'Contents of existing file were unchanged.');

    // Check that no hooks were called while failing.
    $this->assertFileHooksCalled(array());

    // Ensure that the existing file wasn't overwritten.
    $this->assertFileUnchanged($existing, file_load($existing->fid, TRUE));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
