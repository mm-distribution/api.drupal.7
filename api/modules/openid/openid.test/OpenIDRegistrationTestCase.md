# OpenIDRegistrationTestCase

- **Type:** Class
- **File:** [`modules/openid/openid.test`](_file.md), lines 403–577 · [local source](../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L403-L577)
- **Module/theme:** openid

## Signature

```php
class OpenIDRegistrationTestCase extends OpenIDWebTestCase
```

## Documentation

```text
Test account registration using Simple Registration and Attribute Exchange.
```

## Methods (derived index)

- [getInfo()](OpenIDRegistrationTestCase/getInfo.md)
- [setUp()](OpenIDRegistrationTestCase/setUp.md)
- [testRegisterUserWithEmailVerification()](OpenIDRegistrationTestCase/testRegisterUserWithEmailVerification.md) — Test OpenID auto-registration with e-mail verification enabled.
- [testRegisterUserWithoutEmailVerification()](OpenIDRegistrationTestCase/testRegisterUserWithoutEmailVerification.md) — Test OpenID auto-registration with e-mail verification disabled.
- [testRegisterUserWithInvalidSreg()](OpenIDRegistrationTestCase/testRegisterUserWithInvalidSreg.md) — Test OpenID auto-registration with a provider that supplies invalid SREG information (a username that is already taken, and no e-mail address).
- [testRegisterUserWithoutSreg()](OpenIDRegistrationTestCase/testRegisterUserWithoutSreg.md) — Test OpenID auto-registration with a provider that does not supply SREG information (i.e. no username or e-mail address).
- [testRegisterUserWithAXButNoSREG()](OpenIDRegistrationTestCase/testRegisterUserWithAXButNoSREG.md) — Test OpenID auto-registration with a provider that supplies AX information, but no SREG.

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
