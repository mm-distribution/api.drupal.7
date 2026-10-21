# UserPasswordResetTestCase::testUserDirectLogin()

- **Type:** Method
- **File:** [`modules/user/user.test`](../_file.md), lines 802–805 · [local source](../../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L802-L805)
- **Class:** [UserPasswordResetTestCase](../UserPasswordResetTestCase.md)
- **Module/theme:** user

## Signature

```php
function testUserDirectLogin()
```

## Documentation

```text
Test direct login link that bypasses the password reset form.
```

## Code

```php
  function testUserDirectLogin() {
    $this->testUserPasswordReset(TRUE);
    $this->testUserPasswordResetLoggedIn(TRUE);
  }
```

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
