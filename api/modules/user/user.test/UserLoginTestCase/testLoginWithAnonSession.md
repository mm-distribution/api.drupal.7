# UserLoginTestCase::testLoginWithAnonSession()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 453–459 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L453-L459)
- **Class:** [UserLoginTestCase](../UserLoginTestCase.md)
- **Module/theme:** user

## Signature

```php
function testLoginWithAnonSession()
```

## Documentation

```text
Test logging in when an anon session already exists.
```

## Code

```php
  function testLoginWithAnonSession() {
    // Visit the callback to generate a session for this anon user.
    $this->drupalGet('user_session_test_anon_session');
    // Now login.
    $account = $this->drupalCreateUser(array());
    $this->drupalLogin($account);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
