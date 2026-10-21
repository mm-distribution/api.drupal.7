# UserPictureTestCase::testDeletePicture()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1608–1647 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1608-L1647)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testDeletePicture()
```

## Documentation

```text
Tests deletion of user pictures.
```

## Code

```php
  function testDeletePicture() {
    $this->drupalLogin($this->user);

    $image = current($this->drupalGetTestFiles('image'));
    $info = image_get_info($image->uri);

    // Set new variables: valid dimensions, valid filesize (0 = no limit).
    $test_dim = ($info['width'] + 10) . 'x' . ($info['height'] + 10);
    variable_set('user_picture_dimensions', $test_dim);
    variable_set('user_picture_file_size', 0);

    // Save a new picture.
    $edit = array('files[picture_upload]' => drupal_realpath($image->uri));
    $this->drupalPost('user/' . $this->user->uid . '/edit', $edit, t('Save'));

    // Load actual user data from database.
    $account = user_load($this->user->uid, TRUE);
    $pic_path = isset($account->picture) ? $account->picture->uri : NULL;

    // Check if image is displayed in user's profile page.
    $this->drupalGet('user');
    $this->assertRaw(file_uri_target($pic_path), "Image is displayed in user's profile page");

    // Check if file is located in proper directory.
    $this->assertTrue(is_file($pic_path), 'File is located in proper directory');

    $edit = array('picture_delete' => 1);
    $this->drupalPost('user/' . $this->user->uid . '/edit', $edit, t('Save'));

    // Load actual user data from database.
    $account1 = user_load($this->user->uid, TRUE);
    $this->assertNull($account1->picture, 'User object has no picture');

    $file = file_load($account->picture->fid);
    $this->assertFalse($file, 'File is removed from database');

    // Clear out PHP's file stat cache so we see the current value.
    clearstatcache();
    $this->assertFalse(is_file($pic_path), 'File is removed from file system');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
