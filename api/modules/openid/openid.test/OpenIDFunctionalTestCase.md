# OpenIDFunctionalTestCase

- **Type:** Class
- **File:** [`modules/openid/openid.test`](_file.md), lines 42–398 · [local source](../../../../source/modules/openid/openid.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test#L42-L398)
- **Module/theme:** openid

## Signature

```php
class OpenIDFunctionalTestCase extends OpenIDWebTestCase
```

## Documentation

```text
Test discovery and login using OpenID
```

## Properties

### $web_user

```php
protected $web_user;
```

## Methods (derived index)

- [getInfo()](OpenIDFunctionalTestCase/getInfo.md)
- [setUp()](OpenIDFunctionalTestCase/setUp.md)
- [testDiscovery()](OpenIDFunctionalTestCase/testDiscovery.md) — Test discovery of OpenID Provider Endpoint via Yadis and HTML.
- [testLogin()](OpenIDFunctionalTestCase/testLogin.md) — Test login using OpenID.
- [testLoginMaintenanceMode()](OpenIDFunctionalTestCase/testLoginMaintenanceMode.md) — Test login using OpenID during maintenance mode.
- [testDelete()](OpenIDFunctionalTestCase/testDelete.md) — Test deleting an OpenID identity from a user's profile.
- [testBlockedUserLogin()](OpenIDFunctionalTestCase/testBlockedUserLogin.md) — Test that a blocked user cannot log in.
- [addIdentity()](OpenIDFunctionalTestCase/addIdentity.md) — Add OpenID identity to user's profile.
- [addRedirectedIdentity()](OpenIDFunctionalTestCase/addRedirectedIdentity.md) — Add OpenID identity, changed by the following redirects, to user's profile.
- [testSignatureValidation()](OpenIDFunctionalTestCase/testSignatureValidation.md) — Tests that openid.signed is verified.

---
_Drupal 7.103 · [modules/openid/openid.test](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.test) · Licensed GPL-2.0-or-later (see LICENSE)._
