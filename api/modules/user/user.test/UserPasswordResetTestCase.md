# UserPasswordResetTestCase

- **Type:** Class
- **File:** [`modules/user/user.test`](_file.md), lines 522–960 · [local source](../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L522-L960)
- **Module/theme:** user

## Signature

```php
class UserPasswordResetTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests resetting a user password.
```

## Properties

### $profile

```php
protected $profile = 'standard';
```

## Methods (derived index)

- [setUp()](UserPasswordResetTestCase/setUp.md)
- [getInfo()](UserPasswordResetTestCase/getInfo.md)
- [getResetURL()](UserPasswordResetTestCase/getResetURL.md) — Retrieves password reset email and extracts the login link.
- [generateResetURL()](UserPasswordResetTestCase/generateResetURL.md) — Generates login link.
- [getConfirmURL()](UserPasswordResetTestCase/getConfirmURL.md) — Turns a password reset URL into a 'confirm' URL.
- [testUserPasswordReset()](UserPasswordResetTestCase/testUserPasswordReset.md) — Tests password reset functionality.
- [testPasswordResetFloodControlPerUser()](UserPasswordResetTestCase/testPasswordResetFloodControlPerUser.md) — Test user-based flood control on password reset.
- [testPasswordResetFloodControlPerIp()](UserPasswordResetTestCase/testPasswordResetFloodControlPerIp.md) — Test IP-based flood control on password reset.
- [testUserPasswordResetLoggedIn()](UserPasswordResetTestCase/testUserPasswordResetLoggedIn.md) — Test user password reset while logged in.
- [testUserDirectLogin()](UserPasswordResetTestCase/testUserDirectLogin.md) — Test direct login link that bypasses the password reset form.
- [testUserPasswordResetExpired()](UserPasswordResetTestCase/testUserPasswordResetExpired.md) — Attempts login using an expired password reset link.
- [testUserPasswordTextboxNotFilled()](UserPasswordResetTestCase/testUserPasswordTextboxNotFilled.md) — Tests the text box on incorrect login via link to password reset page.
- [testResetImpersonation()](UserPasswordResetTestCase/testResetImpersonation.md) — Make sure that users cannot forge password reset URLs of other users.
- [testResetInvalidation()](UserPasswordResetTestCase/testResetInvalidation.md) — Make sure that password reset URLs are invalidated when the user's email address changes.
- [testUniqueHashNoPasswordValue()](UserPasswordResetTestCase/testUniqueHashNoPasswordValue.md) — Test uniqueness of output from user_pass_rehash() with no passwords.

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
