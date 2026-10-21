# SessionTestCase::testSameSiteCookieAttributeDisabledViaPhpIni()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 417–433 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L417-L433)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSameSiteCookieAttributeDisabledViaPhpIni()
```

## Documentation

```text
Test disabling the samesite attribute on session cookies via php ini
```

## Code

```php
  function testSameSiteCookieAttributeDisabledViaPhpIni() {
    if (\PHP_VERSION_ID < 70300) {
      // There is no session.cookie_samesite in earlier PHP versions.
      $this->pass('This test is only for PHP 7.3 and later.');
      return;
    }
    $user = $this->drupalCreateUser(array('access content'));
    // Send our own login POST so that we can pass a custom header to trigger
    // session_test.module to call ini_set('session.cookie_samesite', $value)
    $headers[] = 'X-Session-Cookie-Ini-Set: *EMPTY*';
    $edit = array(
      'name' => $user->name,
      'pass' => $user->pass_raw,
    );
    $this->drupalPost('user', $edit, t('Log in'), array(), $headers);
    $this->assertFalse(preg_match('/SameSite=/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie has no SameSite attribute (ini).');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
