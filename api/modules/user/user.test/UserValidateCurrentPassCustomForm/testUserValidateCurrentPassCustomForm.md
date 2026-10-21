# UserValidateCurrentPassCustomForm::testUserValidateCurrentPassCustomForm()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2991–3000 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2991-L3000)
- **Class:** [UserValidateCurrentPassCustomForm](../UserValidateCurrentPassCustomForm.md)
- **Module/theme:** user

## Signature

```php
function testUserValidateCurrentPassCustomForm()
```

## Documentation

```text
Tests that user_validate_current_pass can be reused on a custom form.
```

## Code

```php
  function testUserValidateCurrentPassCustomForm() {
    $this->drupalLogin($this->adminUser);

    // Submit the custom form with the admin user using the access user's password.
    $edit = array();
    $edit['user_form_test_field'] = $this->accessUser->name;
    $edit['current_pass'] = $this->accessUser->pass_raw;
    $this->drupalPost('user_form_test_current_password/' . $this->accessUser->uid, $edit, t('Test'));
    $this->assertText(t('The password has been validated and the form submitted successfully.'));
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
