# FileSaveUploadTest::testExistingRename()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 995–1006 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L995-L1006)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExistingRename()
```

## Documentation

```text
Test renaming when uploading over a file that already exists.
```

## Code

```php
  function testExistingRename() {
    $edit = array(
      'file_test_replace' => FILE_EXISTS_RENAME,
      'files[file_test_upload]' => drupal_realpath($this->image->uri)
    );
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
