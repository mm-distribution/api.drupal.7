# UserLoginTestCase::testPerUserLoginFloodControl()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 383–423 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L383-L423)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
function testPerUserLoginFloodControl()
```

## Documentation

```text
Test the per-user login flood control.
```

## Code

```php
  function testPerUserLoginFloodControl() {
    // Set a high global limit out so that it is not relevant in the test.
    variable_set('user_failed_login_ip_limit', 4000);
    // Set the per-user login limit.
    variable_set('user_failed_login_user_limit', 3);

    $user1 = $this->drupalCreateUser(array());
    $incorrect_user1 = clone $user1;
    $incorrect_user1->pass_raw .= 'incorrect';

    $user2 = $this->drupalCreateUser(array());

    // Try 2 failed logins.
    for ($i = 0; $i < 2; $i++) {
      $this->assertFailedLogin($incorrect_user1);
    }

    // A successful login will reset the per-user flood control count.
    $this->drupalLogin($user1);
    $this->drupalLogout();

    // Try 3 failed logins for user 1, they will not trigger flood control.
    for ($i = 0; $i < 3; $i++) {
      $this->assertFailedLogin($incorrect_user1);
    }

    // Try one successful attempt for user 2, it should not trigger any
    // flood control.
    $this->drupalLogin($user2);
    $this->drupalLogout();

    // Try one more attempt for user 1, it should be rejected, even if the
    // correct password has been used.
    $this->assertFailedLogin($user1, 'user');
    $this->resetUserPassword($user1);
    $this->drupalLogout();

    // Try to log in as user 1, it should be successful.
    $this->drupalLogin($user1);
    $this->assertRaw('Member for');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
