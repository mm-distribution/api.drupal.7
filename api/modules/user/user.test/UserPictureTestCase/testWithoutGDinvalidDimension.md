# UserPictureTestCase::testWithoutGDinvalidDimension()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1480–1503 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1480-L1503)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testWithoutGDinvalidDimension()
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
  function testWithoutGDinvalidDimension() {
    if ($this->_directory_test && !image_get_toolkit()) {
      $this->drupalLogin($this->user);

      $image = current($this->drupalGetTestFiles('image'));
      $info = image_get_info($image->uri);

      // Set new variables: invalid dimensions, valid filesize (0 = no limit).
      $test_dim = ($info['width'] - 10) . 'x' . ($info['height'] - 10);
      variable_set('user_picture_dimensions', $test_dim);
      variable_set('user_picture_file_size', 0);

      $pic_path = $this->saveUserPicture($image);

      // Test that the upload failed and that the correct reason was cited.
      $text = t('The specified file %filename could not be uploaded.', array('%filename' => $image->filename));
      $this->assertRaw($text, 'Upload failed.');
      $text = t('The image is too large; the maximum dimensions are %dimensions pixels.', array('%dimensions' => $test_dim));
      $this->assertRaw($text, 'Checking response on invalid image (dimensions).');

      // Check if file is not uploaded.
      $this->assertFalse(is_file($pic_path), 'File was not uploaded.');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
