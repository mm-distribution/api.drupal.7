# UserLoginTestCase::testGlobalLoginFloodControl()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 340–378 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L340-L378)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
function testGlobalLoginFloodControl()
```

## Documentation

```text
Test the global login flood control.
```

## Code

```php
  function testGlobalLoginFloodControl() {
    // Set the global login limit.
    variable_set('user_failed_login_ip_limit', 10);
    // Set a high per-user limit out so that it is not relevant in the test.
    variable_set('user_failed_login_user_limit', 4000);

    $user1 = $this->drupalCreateUser(array());
    $incorrect_user1 = clone $user1;
    $incorrect_user1->pass_raw .= 'incorrect';

    // Try 2 failed logins.
    for ($i = 0; $i < 2; $i++) {
      $this->assertFailedLogin($incorrect_user1);
    }

    // A successful login will not reset the IP-based flood control count.
    $this->drupalLogin($user1);
    $this->drupalLogout();

    // Try 8 more failed logins, they should not trigger the flood control
    // mechanism.
    for ($i = 0; $i < 8; $i++) {
      $this->assertFailedLogin($incorrect_user1);
    }

    // The next login trial should result in an IP-based flood error message.
    $this->assertFailedLogin($incorrect_user1, 'ip');

    // A login with the correct password should also result in a flood error
    // message.
    $this->assertFailedLogin($user1, 'ip');

    // A login attempt after resetting the password should still fail, since the
    // IP-based flood control count is not cleared after a password reset.
    $this->resetUserPassword($user1);
    $this->drupalLogout();
    $this->assertFailedLogin($user1, 'ip');
    $this->assertRaw(t('Sorry, too many failed login attempts from your IP address. This IP address is temporarily blocked. Try again later or <a href="@url">request a new password</a>.', array('@url' => url('user/password'))));
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
