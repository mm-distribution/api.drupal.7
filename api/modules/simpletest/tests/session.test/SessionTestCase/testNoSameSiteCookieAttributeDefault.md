# SessionTestCase::testNoSameSiteCookieAttributeDefault()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 314–333 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L314-L333)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testNoSameSiteCookieAttributeDefault()
```

## Documentation

```text
Test absence of SameSite attribute on session cookies by default.
```

## Code

```php
  function testNoSameSiteCookieAttributeDefault() {
    $user = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user->uid);
    if (\PHP_VERSION_ID < 70300) {
      $this->drupalLogin($user);
    }
    else {
      // PHP often defaults to an empty value for session.cookie_samesite but
      // that may vary, so we set an explicit empty value.
      // Send our own login POST so that we can pass a custom header to trigger
      // session_test.module to call ini_set('session.cookie_samesite', $value)
      $headers[] = 'X-Session-Cookie-Ini-Set: *EMPTY*';
      $edit = array(
        'name' => $user->name,
        'pass' => $user->pass_raw,
      );
      $this->drupalPost('user', $edit, t('Log in'), array(), $headers);
    }
    $this->assertFalse(preg_match('/SameSite=/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie has no SameSite attribute (default).');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
