# UserPictureTestCase::testWithGDinvalidDimension()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1411–1435 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1411-L1435)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testWithGDinvalidDimension()
```

## Documentation

```text
Do the test:
 GD Toolkit is installed
 Picture has invalid dimension

results: The image should be uploaded because ImageGDToolkit resizes the picture
```

## Code

```php
  function testWithGDinvalidDimension() {
    if ($this->_directory_test && image_get_toolkit()) {
      $this->drupalLogin($this->user);

      $image = current($this->drupalGetTestFiles('image'));
      $info = image_get_info($image->uri);

      // Set new variables: invalid dimensions, valid filesize (0 = no limit).
      $test_dim = ($info['width'] - 10) . 'x' . ($info['height'] - 10);
      variable_set('user_picture_dimensions', $test_dim);
      variable_set('user_picture_file_size', 0);

      $pic_path = $this->saveUserPicture($image);
      // Check that the image was resized and is being displayed on the
      // user's profile page.
      $text = t('The image was resized to fit within the maximum allowed dimensions of %dimensions pixels.', array('%dimensions' => $test_dim));
      $this->assertRaw($text, 'Image was resized.');
      $alt = t("@user's picture", array('@user' => format_username($this->user)));
      $style = variable_get('user_picture_style', '');
      $this->assertRaw(check_plain(image_style_url($style, $pic_path)), "Image is displayed in user's edit page");

      // Check if file is located in proper directory.
      $this->assertTrue(is_file($pic_path), "File is located in proper directory");
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
