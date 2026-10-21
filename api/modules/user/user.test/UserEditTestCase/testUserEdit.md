# UserEditTestCase::testUserEdit()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 2266–2323 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L2266-L2323)
- **Class:** [UserEditTestCase](../UserEditTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserEdit()
```

## Documentation

```text
Test user edit page.
```

## Code

```php
  function testUserEdit() {
    // Test user edit functionality with user pictures disabled.
    variable_set('user_pictures', 0);
    $user1 = $this->drupalCreateUser(array('change own username'));
    $user2 = $this->drupalCreateUser(array());
    $this->drupalLogin($user1);

    // Test that error message appears when attempting to use a non-unique user name.
    $edit['name'] = $user2->name;
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t('The name %name is already taken.', array('%name' => $edit['name'])));

    // Repeat the test with user pictures enabled, which modifies the form.
    variable_set('user_pictures', 1);
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t('The name %name is already taken.', array('%name' => $edit['name'])));

    // Check that filling out a single password field does not validate.
    $edit = array();
    $edit['pass[pass1]'] = '';
    $edit['pass[pass2]'] = $this->randomName();
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertText(t("The specified passwords do not match."), 'Typing mismatched passwords displays an error message.');

    $edit['pass[pass1]'] = $this->randomName();
    $edit['pass[pass2]'] = '';
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertText(t("The specified passwords do not match."), 'Typing mismatched passwords displays an error message.');

    // Test that the error message appears when attempting to change the mail or
    // pass without the current password.
    $edit = array();
    $edit['mail'] = $this->randomName() . '@new.example.com';
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t("Your current password is missing or incorrect; it's required to change the %name.", array('%name' => t('E-mail address'))));

    $edit['current_pass'] = $user1->pass_raw;
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));

    // Test that the user must enter current password before changing passwords.
    $edit = array();
    $edit['pass[pass1]'] = $new_pass = $this->randomName();
    $edit['pass[pass2]'] = $new_pass;
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t("Your current password is missing or incorrect; it's required to change the %name.", array('%name' => t('Password'))));

    // Try again with the current password.
    $edit['current_pass'] = $user1->pass_raw;
    $this->drupalPost("user/$user1->uid/edit", $edit, t('Save'));
    $this->assertRaw(t("The changes have been saved."));

    // Make sure the user can log in with their new password.
    $this->drupalLogout();
    $user1->pass_raw = $new_pass;
    $this->drupalLogin($user1);
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
