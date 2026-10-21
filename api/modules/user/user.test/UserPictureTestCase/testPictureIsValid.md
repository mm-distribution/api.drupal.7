# UserPictureTestCase::testPictureIsValid()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1544–1583 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1544-L1583)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testPictureIsValid()
```

## Documentation

```text
Do the test:
 Picture is valid (proper size and dimension)

results: The image should be uploaded
```

## Code

```php
  function testPictureIsValid() {
    if ($this->_directory_test) {
      $this->drupalLogin($this->user);

      $image = current($this->drupalGetTestFiles('image'));
      $info = image_get_info($image->uri);

      // Set new variables: valid dimensions, valid filesize (0 = no limit).
      $test_dim = ($info['width'] + 10) . 'x' . ($info['height'] + 10);
      variable_set('user_picture_dimensions', $test_dim);
      variable_set('user_picture_file_size', 0);

      $pic_path = $this->saveUserPicture($image);

      // Check if image is displayed in user's profile page.
      $this->drupalGet('user');
      $this->assertRaw(file_uri_target($pic_path), "Image is displayed in user's profile page");

      // Check if file is located in proper directory.
      $this->assertTrue(is_file($pic_path), 'File is located in proper directory');

      // Set new picture dimensions.
      $test_dim = ($info['width'] + 5) . 'x' . ($info['height'] + 5);
      variable_set('user_picture_dimensions', $test_dim);

      $pic_path2 = $this->saveUserPicture($image);
      $this->assertNotEqual($pic_path, $pic_path2, 'Filename of second picture is different.');

      // Check if user picture has a valid file ID after saving the user.
      $account = user_load($this->user->uid, TRUE);
      $this->assertTrue(is_object($account->picture), 'User picture object is valid after user load.');
      $this->assertNotNull($account->picture->fid, 'User picture object has a FID after user load.');
      $this->assertTrue(is_file($account->picture->uri), 'File is located in proper directory after user load.');
      user_save($account);
      // Verify that the user save does not destroy the user picture object.
      $this->assertTrue(is_object($account->picture), 'User picture object is valid after user save.');
      $this->assertNotNull($account->picture->fid, 'User picture object has a FID after user save.');
      $this->assertTrue(is_file($account->picture->uri), 'File is located in proper directory after user save.');
    }
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
