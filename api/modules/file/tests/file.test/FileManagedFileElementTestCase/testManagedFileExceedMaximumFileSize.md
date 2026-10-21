# FileManagedFileElementTestCase::testManagedFileExceedMaximumFileSize()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 496–511 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L496-L511)
- **Class:** [FileManagedFileElementTestCase](../FileManagedFileElementTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testManagedFileExceedMaximumFileSize()
```

## Documentation

```text
Tests uploading a file that exceeds the maximum file size.
```

## Code

```php
  function testManagedFileExceedMaximumFileSize() {
    $path = 'file/test/0/0';
    $this->drupalGet($path);

    // Create a test file that exceeds the maximum POST size with 1 kilobyte.
    $post_max_size = $this->_postMaxSizeToInteger(ini_get('post_max_size'));
    $filename = 'text-exceeded';
    simpletest_generate_file($filename, ceil(($post_max_size + 1024) / 1024), 1024, 'text');
    $uri = 'public://' . $filename . '.txt';
    $input_base_name = 'file';
    $edit = array('files[' . $input_base_name . ']' => drupal_realpath($uri));
    $this->drupalPostAJAX(NULL, $edit, $input_base_name . '_upload_button');
    $this->assertFieldByXpath('//input[@type="submit"]', t('Upload'), 'After uploading a file that exceeds the maximum file size, the "Upload" button is displayed.');
    $this->drupalPost($path, array(), t('Save'));
    $this->assertRaw(t('The file id is %fid.', array('%fid' => 0)), 'Submitted without a file.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
