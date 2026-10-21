# UserPasswordResetTestCase::testPasswordResetFloodControlPerUser()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 658–703 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L658-L703)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testPasswordResetFloodControlPerUser()
```

## Documentation

```text
Test user-based flood control on password reset.
```

## Code

```php
  function testPasswordResetFloodControlPerUser() {
    // Set a very low limit for testing.
    variable_set('user_pass_reset_user_limit', 2);

    // Create a user.
    $account = $this->drupalCreateUser();
    $this->drupalLogin($account);
    $this->drupalLogout();

    $edit = array('name' => $account->name);

    // Try 2 requests that should not trigger flood control.
    for ($i = 0; $i < 2; $i++) {
      $this->drupalPost('user/password', $edit, t('E-mail new password'));
      // Confirm the password reset.
      $password_reset_text = variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.'));
      $this->assertRaw(format_string($password_reset_text, array('%identifier' => $account->name)), 'Password reset instructions mailed message displayed.');
      // Ensure that flood control was not triggered.
      $this->assertNoText(t('is temporarily blocked. Try again later'), 'Flood control was not triggered by password reset.');
    }

    // A successful password reset should clear flood events.
    $resetURL = $this->getResetURL();
    $this->drupalGet($resetURL);

    // Check successful login.
    $this->drupalPost(NULL, NULL, t('Log in'));
    $this->drupalLogout();

    // Try 2 requests that should not trigger flood control.
    for ($i = 0; $i < 2; $i++) {
      $this->drupalPost('user/password', $edit, t('E-mail new password'));
      // Confirm the password reset.
      $password_reset_text = variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.'));
      $this->assertRaw(format_string($password_reset_text, array('%identifier' => $account->name)), 'Password reset instructions mailed message displayed.');
      // Ensure that flood control was not triggered.
      $this->assertNoText(t('is temporarily blocked. Try again later'), 'Flood control was not triggered by password reset.');
    }

    // The next request should trigger flood control
    $this->drupalPost('user/password', $edit, t('E-mail new password'));
    // Confirm the password reset was blocked.
    $this->assertNoText(t('Further instructions have been sent to your e-mail address.'), 'Password reset instructions mailed message not displayed for excessive password resets.');
    // Ensure that flood control was triggered.
    $this->assertText(t('Sorry, there have been more than 2 password reset attempts for this account. It is temporarily blocked.'), 'Flood control was triggered by excessive password resets for one user.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
