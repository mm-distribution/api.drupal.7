# UserPictureTestCase::setUp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1374–1392 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1374-L1392)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    // Enable user pictures.
    variable_set('user_pictures', 1);

    $this->user = $this->drupalCreateUser();

    // Test if directories specified in settings exist in filesystem.
    $file_dir = 'public://';
    $file_check = file_prepare_directory($file_dir, FILE_CREATE_DIRECTORY);
    // TODO: Test public and private methods?

    $picture_dir = variable_get('user_picture_path', 'pictures');
    $picture_path = $file_dir . $picture_dir;

    $pic_check = file_prepare_directory($picture_path, FILE_CREATE_DIRECTORY);
    $this->_directory_test = is_writable($picture_path);
    $this->assertTrue($this->_directory_test, "The directory $picture_path doesn't exist or is not writable. Further tests won't be made.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
