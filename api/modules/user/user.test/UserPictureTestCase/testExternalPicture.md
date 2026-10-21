# UserPictureTestCase::testExternalPicture()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1588–1603 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1588-L1603)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testExternalPicture()
```

## Documentation

```text
Test HTTP schema working with user pictures.
```

## Code

```php
  function testExternalPicture() {
    $this->drupalLogin($this->user);
    // Set the default picture to an URI with a HTTP schema.
    $images = $this->drupalGetTestFiles('image');
    $image = $images[0];
    $pic_path = file_create_url($image->uri);
    variable_set('user_picture_default', $pic_path);

    // Check if image is displayed in user's profile page.
    $this->drupalGet('user');

    // Get the user picture image via xpath.
    $elements = $this->xpath('//div[@class="user-picture"]/img');
    $this->assertEqual(count($elements), 1, "There is exactly one user picture on the user's profile page");
    $this->assertEqual($pic_path, (string) $elements[0]['src'], "User picture source is correct.");
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
