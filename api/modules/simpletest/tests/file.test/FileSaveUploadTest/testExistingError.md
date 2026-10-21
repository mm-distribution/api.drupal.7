# FileSaveUploadTest::testExistingError()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 1027–1038 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L1027-L1038)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingError()
```

## Documentation

```text
Test for failure when uploading over a file that already exists.
```

## Code

```php
  function testExistingError() {
    $edit = array(
      'file_test_replace' => FILE_EXISTS_ERROR,
      'files[file_test_upload]' => drupal_realpath($this->image->uri)
    );
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('Epic upload FAIL!'), 'Found the failure message.');

    // Check that the no hooks were called while failing.
    $this->assertFileHooksCalled(array());
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
