# UserPictureTestCase::testUserPictureAdminFormValidation()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 1661–1674 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1661-L1674)
- **Class:** [UserPictureTestCase](../UserPictureTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserPictureAdminFormValidation()
```

## Documentation

```text
Tests the admin form validates user picture settings.
```

## Code

```php
  function testUserPictureAdminFormValidation() {
    $this->drupalLogin($this->drupalCreateUser(array('administer users')));

    // The default values are valid.
    $this->drupalPost('admin/config/people/accounts', array(), t('Save configuration'));
    $this->assertText(t('The configuration options have been saved.'), 'The default values are valid.');

    // The form does not save with an invalid file size.
    $edit = array(
      'user_picture_file_size' => $this->randomName(),
    );
    $this->drupalPost('admin/config/people/accounts', $edit, t('Save configuration'));
    $this->assertNoText(t('The configuration options have been saved.'), 'The form does not save with an invalid file size.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
