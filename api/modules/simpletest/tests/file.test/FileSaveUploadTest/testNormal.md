# FileSaveUploadTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 628–676 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L628-L676)
- **Class:** [FileSaveUploadTest](../FileSaveUploadTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNormal()
```

## Documentation

```text
Test the file_save_upload() function.
```

## Code

```php
  function testNormal() {
    $max_fid_after = db_query('SELECT MAX(fid) AS fid FROM {file_managed}')->fetchField();
    $this->assertTrue($max_fid_after > $this->maxFidBefore, 'A new file was created.');
    $file1 = file_load($max_fid_after);
    $this->assertTrue($file1, 'Loaded the file.');
    // MIME type of the uploaded image may be either image/jpeg or image/png.
    $this->assertEqual(substr($file1->filemime, 0, 5), 'image', 'A MIME type was set.');

    // Reset the hook counters to get rid of the 'load' we just called.
    file_test_reset();

    // Upload a second file.
    $max_fid_before = db_query('SELECT MAX(fid) AS fid FROM {file_managed}')->fetchField();
    $image2 = current($this->drupalGetTestFiles('image'));
    $edit = array('files[file_test_upload]' => drupal_realpath($image2->uri));
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('You WIN!'));
    $max_fid_after = db_query('SELECT MAX(fid) AS fid FROM {file_managed}')->fetchField();

    // Check that the correct hooks were called.
    $this->assertFileHooksCalled(array('validate', 'insert'));

    $file2 = file_load($max_fid_after);
    $this->assertTrue($file2);
    // MIME type of the uploaded image may be either image/jpeg or image/png.
    $this->assertEqual(substr($file2->filemime, 0, 5), 'image', 'A MIME type was set.');

    // Load both files using file_load_multiple().
    $files = file_load_multiple(array($file1->fid, $file2->fid));
    $this->assertTrue(isset($files[$file1->fid]), 'File was loaded successfully');
    $this->assertTrue(isset($files[$file2->fid]), 'File was loaded successfully');

    // Upload a third file to a subdirectory.
    $image3 = current($this->drupalGetTestFiles('image'));
    $image3_realpath = drupal_realpath($image3->uri);
    $dir = $this->randomName();
    $edit = array(
      'files[file_test_upload]' => $image3_realpath,
      'file_subdir' => $dir,
    );
    $this->drupalPost('file-test/upload', $edit, t('Submit'));
    $this->assertResponse(200, 'Received a 200 response for posted test file.');
    $this->assertRaw(t('You WIN!'));
    $this->assertTrue(is_file('temporary://' . $dir . '/' . trim(drupal_basename($image3_realpath))));

    // Check that file_load_multiple() with no arguments returns FALSE.
    $this->assertFalse(file_load_multiple(), 'No files were loaded.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
