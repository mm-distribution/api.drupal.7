# SessionTestCase::testSamesiteCookiePhpSettingLax()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 439–455 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L439-L455)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSamesiteCookiePhpSettingLax()
```

## Documentation

```text
Test that a PHP setting for session.cookie_samesite is not overridden by
the default value in Drupal, without a samesite_cookie_value variable.
```

## Code

```php
  function testSamesiteCookiePhpSettingLax() {
    if (\PHP_VERSION_ID < 70300) {
      // There is no session.cookie_samesite in earlier PHP versions.
      $this->pass('This test is only for PHP 7.3 and later.');
      return;
    }
    $user = $this->drupalCreateUser(array('access content'));
    // Send our own login POST so that we can pass a custom header to trigger
    // session_test.module to call ini_set('session.cookie_samesite', $value)
    $headers[] = 'X-Session-Cookie-Ini-Set: Lax';
    $edit = array(
      'name' => $user->name,
      'pass' => $user->pass_raw,
    );
    $this->drupalPost('user', $edit, t('Log in'), array(), $headers);
    $this->assertTrue(preg_match('/SameSite=Lax/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie is set as SameSite=Lax.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
