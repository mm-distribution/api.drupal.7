# UserPictureTestCase::saveUserPicture()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1649–1656 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1649-L1656)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function saveUserPicture($image)
```

## Documentation

_No docblock in source._

## Code

```php
  function saveUserPicture($image) {
    $edit = array('files[picture_upload]' => drupal_realpath($image->uri));
    $this->drupalPost('user/' . $this->user->uid . '/edit', $edit, t('Save'));

    // Load actual user data from database.
    $account = user_load($this->user->uid, TRUE);
    return isset($account->picture) ? $account->picture->uri : NULL;
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
