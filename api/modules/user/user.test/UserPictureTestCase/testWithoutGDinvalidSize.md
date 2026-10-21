# UserPictureTestCase::testWithoutGDinvalidSize()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1512–1536 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1512-L1536)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testWithoutGDinvalidSize()
```

## Documentation

```text
Do the test:
 GD Toolkit is not installed
 Picture has invalid size

results: The image shouldn't be uploaded
```

## Code

```php
  function testWithoutGDinvalidSize() {
    if ($this->_directory_test && !image_get_toolkit()) {
      $this->drupalLogin($this->user);

      $image = current($this->drupalGetTestFiles('image'));
      $info = image_get_info($image->uri);

      // Set new variables: valid dimensions, invalid filesize.
      $test_dim = ($info['width'] + 10) . 'x' . ($info['height'] + 10);
      $test_size = 1;
      variable_set('user_picture_dimensions', $test_dim);
      variable_set('user_picture_file_size', $test_size);

      $pic_path = $this->saveUserPicture($image);

      // Test that the upload failed and that the correct reason was cited.
      $text = t('The specified file %filename could not be uploaded.', array('%filename' => $image->filename));
      $this->assertRaw($text, 'Upload failed.');
      $text = t('The file is %filesize exceeding the maximum file size of %maxsize.', array('%filesize' => format_size(filesize($image->uri)), '%maxsize' => format_size($test_size * 1024)));
      $this->assertRaw($text, 'File size cited as reason for failure.');

      // Check if file is not uploaded.
      $this->assertFalse(is_file($pic_path), 'File was not uploaded.');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
