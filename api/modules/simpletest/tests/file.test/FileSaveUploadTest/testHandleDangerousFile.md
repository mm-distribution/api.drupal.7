# FileSaveUploadTest::testHandleDangerousFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 763–832 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L763-L832)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testHandleDangerousFile()
```

## Documentation

```text
Test dangerous file handling.
```

## Code

```php
  function testHandleDangerousFile() {
    // Allow the .php extension and make sure it gets munged and given a .txt
    // extension for safety. Also check to make sure its MIME type was changed.
    $edit = array(
      'file_test_replace' => FILE_EXISTS_REPLACE,
      'files[file_test_upload]' => drupal_realpath($this->phpfile->uri),
      'is_image_file' => FALSE,
      'extensions' => 'php',
    );

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $message = t('For security reasons, your upload has been renamed to') . ' <em class="placeholder">' . $this->phpfile->filename . '_.txt' . '</em>';
    $this->assertRaw($message, 'Dangerous file was renamed.');
    $this->assertRaw('File name is php-2.php_.txt.');
    $this->assertRaw(t('File MIME type is text/plain.'), "Dangerous file's MIME type was changed.");
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Ensure dangerous files are not renamed when insecure uploads is TRUE.
    // Turn on insecure uploads.
    variable_set('allow_insecure_uploads', 1);
    // Reset the hook counters.
    file_test_reset();

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertNoRaw(t('For security reasons, your upload has been renamed'), 'Found no security message.');
    $this->assertRaw(t('File name is !filename', array('!filename' => $this->phpfile->filename)), 'Dangerous file was not renamed when insecure uploads is TRUE.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Reset the hook counters.
    file_test_reset();

    // Even with insecure uploads allowed, the .php file should not be uploaded
    // if it is not explicitly included in the list of allowed extensions.
    $edit['extensions'] = 'foo';
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $message = t('Only files with the following extensions are allowed:') . ' <em class="placeholder">' . $edit['extensions'] . '</em>';
    $this->assertRaw($message, 'Cannot upload a disallowed extension');
    $this->assertRaw(t('Epic upload FAIL!'), 'Found the failure message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate'));

    // Reset the hook counters.
    file_test_reset();

    // Turn off insecure uploads, then try the same thing as above (ensure that
    // the .php file is still rejected since it's not in the list of allowed
    // extensions).
    variable_set('allow_insecure_uploads', 0);
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $message = t('Only files with the following extensions are allowed:') . ' <em class="placeholder">' . $edit['extensions'] . '</em>';
    $this->assertRaw($message, 'Cannot upload a disallowed extension');
    $this->assertRaw(t('Epic upload FAIL!'), 'Found the failure message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate'));

    // Reset the hook counters.
    file_test_reset();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
