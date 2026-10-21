# UserLoginTestCase

- **Type:** Class
- **File:** [`modules/user/user.test`](_file.md), lines 324–517 · [local source](../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L324-L517)
- **Module/theme:** user

## Signature

```php
class UserLoginTestCase extends DrupalWebTestCase
```

## Documentation

```text
Functional tests for user logins, including rate limiting of login attempts.
```

## Methods (derived index)

- [getInfo()](UserLoginTestCase/getInfo.md)
- [setUp()](UserLoginTestCase/setUp.md)
- [testGlobalLoginFloodControl()](UserLoginTestCase/testGlobalLoginFloodControl.md) — Test the global login flood control.
- [testPerUserLoginFloodControl()](UserLoginTestCase/testPerUserLoginFloodControl.md) — Test the per-user login flood control.
- [testPasswordRehashOnLogin()](UserLoginTestCase/testPasswordRehashOnLogin.md) — Test that user password is re-hashed upon login after changing $count_log2.
- [testLoginWithAnonSession()](UserLoginTestCase/testLoginWithAnonSession.md) — Test logging in when an anon session already exists.
- [assertFailedLogin()](UserLoginTestCase/assertFailedLogin.md) — Make an unsuccessful login attempt.
- [resetUserPassword()](UserLoginTestCase/resetUserPassword.md) — Resets the user password and logs the user in.

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
