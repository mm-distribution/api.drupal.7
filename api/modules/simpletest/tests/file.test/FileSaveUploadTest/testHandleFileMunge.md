# FileSaveUploadTest::testHandleFileMunge()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 837–990 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L837-L990)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testHandleFileMunge()
```

## Documentation

```text
Test file munge handling.
```

## Code

```php
  function testHandleFileMunge() {
    // Ensure insecure uploads are disabled for this test.
    variable_set('allow_insecure_uploads', 0);
    $original_image_uri = $this->image->uri;
    $this->image = file_move($this->image, $this->image->uri . '.foo.' . $this->image_extension);

    // Reset the hook counters to get rid of the 'move' we just called.
    file_test_reset();

    $extensions = $this->image_extension;
    $edit = array(
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'extensions' => $extensions,
    );

    $munged_filename = $this->image->filename;
    $munged_filename = substr($munged_filename, 0, strrpos($munged_filename, '.'));
    $munged_filename .= '_.' . $this->image_extension;

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('For security reasons, your upload has been renamed'), 'Found security message.');
    $this->assertRaw(t('File name is !filename', array('!filename' => $munged_filename)), 'File was successfully munged.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Reset the hook counters.
    file_test_reset();

    // Ensure we don't munge the .foo extension if it is in the list of allowed
    // extensions.
    $extensions = 'foo ' . $this->image_extension;
    $edit = array(
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'extensions' => $extensions,
    );

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertNoRaw(t('For security reasons, your upload has been renamed'), 'Found no security message.');
    $this->assertRaw(t('File name is @filename', array('@filename' => 'image-test.png.foo.png')), 'File was not munged when all extensions within it are allowed.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Ensure we don't munge files if we're allowing any extension.
    // Reset the hook counters.
    file_test_reset();

    $edit = array(
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'allow_all_extensions' => 'empty_array',
    );

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertNoRaw(t('For security reasons, your upload has been renamed'), 'Found no security message.');
    $this->assertRaw(t('File name is !filename', array('!filename' => $this->image->filename)), 'File was not munged when allowing any extension.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Test that a dangerous extension such as .php is munged even if it is in
    // the list of allowed extensions.
    $this->image = file_move($this->image, $original_image_uri . '.php.' . $this->image_extension);
    // Reset the hook counters.
    file_test_reset();

    $extensions = 'php ' . $this->image_extension;
    $edit = array(
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'extensions' => $extensions,
    );

    $munged_filename = $this->image->filename;
    $munged_filename = substr($munged_filename, 0, strrpos($munged_filename, '.'));
    $munged_filename .= '_.' . $this->image_extension;

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('For security reasons, your upload has been renamed'), 'Found security message.');
    $this->assertRaw(t('File name is @filename', array('@filename' => $munged_filename)), 'File was successfully munged.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Reset the hook counters.
    file_test_reset();

    // Dangerous extensions are munged even when all extensions are allowed.
    $edit = array(
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'allow_all_extensions' => 'empty_array',
    );

    $munged_filename = $this->image->filename;
    $munged_filename = substr($munged_filename, 0, strrpos($munged_filename, '.'));
    $munged_filename .= '_.' . $this->image_extension;

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('For security reasons, your upload has been renamed'), 'Found security message.');
    $this->assertRaw(t('File name is @filename.', array('@filename' => 'image-test.png_.php_.png_.txt')), 'File was successfully munged.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Dangerous extensions are munged if is renamed to end in .txt.
    $this->image = file_move($this->image, $original_image_uri . '.cgi.' . $this->image_extension . '.txt');
    // Reset the hook counters.
    file_test_reset();

    $edit = array(
      'files[file_test_upload]' => drupal_realpath($this->image->uri),
      'allow_all_extensions' => 'empty_array',
    );

    $munged_filename = $this->image->filename;
    $munged_filename = substr($munged_filename, 0, strrpos($munged_filename, '.'));
    $munged_filename .= '_.' . $this->image_extension;

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('For security reasons, your upload has been renamed'), 'Found security message.');
    $this->assertRaw(t('File name is @filename.', array('@filename' => 'image-test.png_.cgi_.png_.txt')), 'File was successfully munged.');
    $this->assertRaw(t('You WIN!'), 'Found the success message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    // Reset the hook counters.
    file_test_reset();

    // Ensure that setting $validators['file_validate_extensions'] = array('')
    // rejects all files without munging or renaming.
    $edit = array(
        'files[file_test_upload]' => drupal_realpath($this->image->uri),
        'allow_all_extensions' => 'empty_string',
    );

    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertNoRaw(t('For security reasons, your upload has been renamed'), 'Found security message.');
    $this->assertRaw(t('Epic upload FAIL!'), 'Found the failure message.');

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
