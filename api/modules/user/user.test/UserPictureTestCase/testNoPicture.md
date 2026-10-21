# UserPictureTestCase::testNoPicture()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1394–1402 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1394-L1402)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testNoPicture()
```

## Documentation

_No docblock in source._

## Code

```php
  function testNoPicture() {
    $this->drupalLogin($this->user);

    // Try to upload a file that is not an image for the user picture.
    $not_an_image = $this->drupalGetTestFiles('html');
    $this->saveUserPicture($not_an_image[1]);
    $this->assertRaw(t('Only JPEG, PNG and GIF images are allowed.'), 'Non-image files are not accepted.');
    $this->assertNoRaw(t('Only files with the following extensions are allowed:'), 'Additional error message not displayed.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
