# UserRegistrationTestCase::testRegistrationWithoutEmailVerification()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 52–109 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L52-L109)
- **Class:** [UserRegistrationTestCase](../UserRegistrationTestCase.md)
- **Module/theme:** user

## Signature

```php
function testRegistrationWithoutEmailVerification()
```

## Documentation

_No docblock in source._

## Code

```php
  function testRegistrationWithoutEmailVerification() {
    // Don't require e-mail verification.
    variable_set('user_email_verification', FALSE);

    // Allow registration by site visitors without administrator approval.
    variable_set('user_register', USER_REGISTER_VISITORS);
    $edit = array();
    $edit['name'] = $name = $this->randomName();
    $edit['mail'] = $mail = $edit['name'] . '@example.com';

    // Try entering a mismatching password.
    $edit['pass[pass1]'] = '99999.0';
    $edit['pass[pass2]'] = '99999';
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $this->assertText(t('The specified passwords do not match.'), 'Typing mismatched passwords displays an error message.');

    // Enter a correct password.
    $edit['pass[pass1]'] = $new_pass = $this->randomName();
    $edit['pass[pass2]'] = $new_pass;
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
    $new_user = reset($accounts);
    $this->assertText(t('Registration successful. You are now logged in.'), 'Users are logged in after registering.');
    $this->drupalLogout();

    // Allow registration by site visitors, but require administrator approval.
    variable_set('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL);
    $edit = array();
    $edit['name'] = $name = $this->randomName();
    $edit['mail'] = $mail = $edit['name'] . '@example.com';
    $edit['pass[pass1]'] = $pass = $this->randomName();
    $edit['pass[pass2]'] = $pass;
    $this->drupalPost('user/register', $edit, t('Create new account'));
    $this->assertText(t('Thank you for applying for an account. Your account is currently pending approval by the site administrator.'), 'Users are notified of pending approval');

    // Try to login before administrator approval.
    $auth = array(
      'name' => $name,
      'pass' => $pass,
    );
    $this->drupalPost('user/login', $auth, t('Log in'));
    $this->assertText(t('The username @name has not been activated or is blocked.', array('@name' => $name)), 'User cannot login yet.');

    // Activate the new account.
    $accounts = user_load_multiple(array(), array('name' => $name, 'mail' => $mail));
    $new_user = reset($accounts);
    $admin_user = $this->drupalCreateUser(array('administer users'));
    $this->drupalLogin($admin_user);
    $edit = array(
      'status' => 1,
    );
    $this->drupalPost('user/' . $new_user->uid . '/edit', $edit, t('Save'));
    $this->drupalLogout();

    // Login after administrator approval.
    $this->drupalPost('user/login', $auth, t('Log in'));
    $this->assertText(t('Member for'), 'User can log in after administrator approval.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
