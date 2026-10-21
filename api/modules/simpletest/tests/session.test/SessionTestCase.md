# SessionTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/session.test`](_file.md), lines 8–547 · [local source](../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L8-L547)
- **Module/theme:** batch_test

## Signature

```php
class SessionTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $_logged_in

```php
protected $_logged_in;
```

## Methods (derived index)

- [getInfo()](SessionTestCase/getInfo.md)
- [setUp()](SessionTestCase/setUp.md)
- [testSessionSaveRegenerate()](SessionTestCase/testSessionSaveRegenerate.md) — Tests for drupal_save_session() and drupal_session_regenerate().
- [testDataPersistence()](SessionTestCase/testDataPersistence.md) — Test data persistence via the session_test module callbacks.
- [testEmptyAnonymousSession()](SessionTestCase/testEmptyAnonymousSession.md) — Test that empty anonymous sessions are destroyed.
- [testSessionWrite()](SessionTestCase/testSessionWrite.md) — Test that sessions are only saved when necessary.
- [testEmptySessionID()](SessionTestCase/testEmptySessionID.md) — Test that empty session IDs are not allowed.
- [testHashedSessionIds()](SessionTestCase/testHashedSessionIds.md) — Test hashing of session ids in the database.
- [testHashedSessionIdsOptOut()](SessionTestCase/testHashedSessionIdsOptOut.md) — Test opt-out of hashing of session ids in the database.
- [testNoSameSiteCookieAttributeDefault()](SessionTestCase/testNoSameSiteCookieAttributeDefault.md) — Test absence of SameSite attribute on session cookies by default.
- [testSameSiteCookieAttributeNoneSecure()](SessionTestCase/testSameSiteCookieAttributeNoneSecure.md) — Test SameSite attribute = None by default on Secure session cookies.
- [testSameSiteCookieAttributeNone()](SessionTestCase/testSameSiteCookieAttributeNone.md) — Test SameSite attribute = None on session cookies.
- [testSameSiteCookieAttributeLax()](SessionTestCase/testSameSiteCookieAttributeLax.md) — Test SameSite attribute = Lax on session cookies.
- [testSameSiteCookieAttributeStrict()](SessionTestCase/testSameSiteCookieAttributeStrict.md) — Test SameSite attribute = Strict on session cookies.
- [testSameSiteCookieAttributeDisabledViaConf()](SessionTestCase/testSameSiteCookieAttributeDisabledViaConf.md) — Test disabling the samesite attribute on session cookies via $conf
- [testSameSiteCookieAttributeDisabledViaPhpIni()](SessionTestCase/testSameSiteCookieAttributeDisabledViaPhpIni.md) — Test disabling the samesite attribute on session cookies via php ini
- [testSamesiteCookiePhpSettingLax()](SessionTestCase/testSamesiteCookiePhpSettingLax.md) — Test that a PHP setting for session.cookie_samesite is not overridden by the default value in Drupal, without a samesite_cookie_value variable.
- [testSamesiteCookieOverrideLaxToStrict()](SessionTestCase/testSamesiteCookieOverrideLaxToStrict.md) — Test overriding the PHP setting for session.cookie_samesite with the samesite_cookie_value variable.
- [testSamesiteCookieLogoutLax()](SessionTestCase/testSamesiteCookieLogoutLax.md) — Test SameSite attribute = Lax on set-cookie header on logout.
- [sessionReset()](SessionTestCase/sessionReset.md) — Reset the cookie file so that it refers to the specified user.
- [assertSessionCookie()](SessionTestCase/assertSessionCookie.md) — Assert whether the SimpleTest browser sent a session cookie.
- [assertSessionEmpty()](SessionTestCase/assertSessionEmpty.md) — Assert whether $_SESSION is empty at the beginning of the request.
- [httpsUrl()](SessionTestCase/httpsUrl.md) — Builds a URL for submitting a mock HTTPS request to HTTP test environments.

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
