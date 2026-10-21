# UserPictureTestCase::testWithGDinvalidSize()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1444–1471 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1444-L1471)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testWithGDinvalidSize()
```

## Documentation

```text
Do the test:
 GD Toolkit is installed
 Picture has invalid size

results: The image should be uploaded because ImageGDToolkit resizes the picture
```

## Code

```php
  function testWithGDinvalidSize() {
    if ($this->_directory_test && image_get_toolkit()) {
      $this->drupalLogin($this->user);

      // Images are sorted first by size then by name. We need an image
      // bigger than 1 KB so we'll grab the last one.
      $files = $this->drupalGetTestFiles('image');
      $image = end($files);
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
      $this->assertFalse(is_file((string) $pic_path), 'File was not uploaded.');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
