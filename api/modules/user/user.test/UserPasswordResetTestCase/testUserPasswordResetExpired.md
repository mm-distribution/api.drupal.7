# UserPasswordResetTestCase::testUserPasswordResetExpired()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 810–827 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L810-L827)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserPasswordResetExpired()
```

## Documentation

```text
Attempts login using an expired password reset link.
```

## Code

```php
  function testUserPasswordResetExpired() {
    // Set password reset timeout variable to 43200 seconds = 12 hours.
    $timeout = 43200;
    variable_set('user_password_reset_timeout', $timeout);

    // Create a user.
    $account = $this->drupalCreateUser();
    $this->drupalLogin($account);
    // Load real user object.
    $account = user_load($account->uid, TRUE);
    $this->drupalLogout();

    // To attempt an expired password reset, create a password reset link as if
    // its request time was 60 seconds older than the allowed limit of timeout.
    $bogus_timestamp = REQUEST_TIME - variable_get('user_password_reset_timeout', 86400) - 60;
    $this->drupalGet("user/reset/$account->uid/$bogus_timestamp/" . user_pass_rehash($account->pass, $bogus_timestamp, $account->login, $account->uid, $account->mail));
    $this->assertText(t('You have tried to use a one-time login link that has expired. Please request a new one using the form below.'), 'Expired password reset request rejected.');
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
