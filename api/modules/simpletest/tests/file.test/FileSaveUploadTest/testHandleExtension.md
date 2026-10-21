# FileSaveUploadTest::testHandleExtension()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 681–758 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L681-L758)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testHandleExtension()
```

## Documentation

```text
Test extension handling.
```

## Code

```php
  function testHandleExtension() {
    // The file being tested is a .gif which is in the default safe list
    // of extensions to allow when the extension validator isn't used. This is
    // implicitly tested at the testNormal() test. Here we tell
    // file_save_upload() to only allow ".foo".
    $extensions = 'foo';
    $edit = array(
      'file_test_replace' => FILE_EXISTS_REPLACE,
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'extensions' => $extensions,
    );

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $message = t('Only files with the following extensions are allowed:') . ' <em class="placeholder">' . $extensions . '</em>';
    $this->assertRaw($message, 'Cannot upload a disallowed extension');
    $this->assertRaw(t('Epic upload FAIL!'), 'Found the failure message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate'));

    // Reset the hook counters.
    file_test_reset();

    $extensions = 'foo ' . $this->image_extension;
    // Now tell file_save_upload() to allow the extension of our test image.
    $edit = array(
      'file_test_replace' => FILE_EXISTS_REPLACE,
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'extensions' => $extensions,
    );

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertNoRaw(t('Only files with the following extensions are allowed:'), 'Can upload an allowed extension.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'load', 'update'));

    // Reset the hook counters.
    file_test_reset();

    // Now tell file_save_upload() to allow any extension.
    $edit = array(
      'file_test_replace' => FILE_EXISTS_REPLACE,
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'allow_all_extensions' => 'empty_array',
    );
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertNoRaw(t('Only files with the following extensions are allowed:'), 'Can upload any extension.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'load', 'update'));

    // Reset the hook counters.
    file_test_reset();

    // Now tell file_save_upload() to allow any extension and try and upload a
    // malicious file.
    $edit = array(
      'file_test_replace' => FILE_EXISTS_REPLACE,
      'files[file_test_upload]' => drupal_realpath($this->phpfile->uri),
      'is_image_file' => FALSE,
      'allow_all_extensions' => 'empty_array',
    );
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $message = t('For security reasons, your upload has been renamed to') . ' <em class="placeholder">' . $this->phpfile->filename . '_.txt' . '</em>';
    $this->assertRaw($message, 'Dangerous file was renamed.');
    $this->assertText('File name is php-2.php_.txt.');
    $this->assertRaw(t('File MIME type is text/plain.'), "Dangerous file's MIME type was changed.");
    $this->assertRaw(t('You WIN!'), 'Found the success message.');
    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
