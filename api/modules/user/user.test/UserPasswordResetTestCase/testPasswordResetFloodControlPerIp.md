# UserPasswordResetTestCase::testPasswordResetFloodControlPerIp()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 708–733 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L708-L733)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testPasswordResetFloodControlPerIp()
```

## Documentation

```text
Test IP-based flood control on password reset.
```

## Code

```php
  function testPasswordResetFloodControlPerIp() {
    // Set a very low limit for testing.
    variable_set('user_pass_reset_ip_limit', 2);

    // Try 2 requests that should not trigger flood control.
    for ($i = 0; $i < 2; $i++) {
      $name = $this->randomName();
      $edit = array('name' => $name);
      $this->drupalPost('user/password', $edit, t('E-mail new password'));
      // Confirm the password reset was not blocked.
      $password_reset_text = variable_get('user_password_reset_text', t('If %identifier is a valid account, an email will be sent with instructions to reset your password.'));
      $this->assertRaw(format_string($password_reset_text, array('%identifier' => $name)), 'Password reset instructions mailed message displayed.');
      // Ensure that flood control was not triggered.
      $this->assertNoText(t('is temporarily blocked. Try again later'), 'Flood control was not triggered by password reset.');
    }

    // The next request should trigger flood control
    $name = $this->randomName();
    $edit = array('name' => $name);
    $this->drupalPost('user/password', $edit, t('E-mail new password'));
    // Confirm the password reset was blocked early. Note that @name is used
    // instead of %name as assertText() works with plain text not HTML.
    $this->assertNoText(t('Sorry, @name is not recognized as a user name or an e-mail address.', array('@name' => $name)), 'User name not recognized message not displayed.');
    // Ensure that flood control was triggered.
    $this->assertText(t('Sorry, too many password reset attempts from your IP address. This IP address is temporarily blocked.'), 'Flood control was triggered by excessive password resets from one IP.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
