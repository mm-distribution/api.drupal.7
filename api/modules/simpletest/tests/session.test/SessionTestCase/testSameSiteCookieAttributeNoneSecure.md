# SessionTestCase::testSameSiteCookieAttributeNoneSecure()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 338–355 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L338-L355)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSameSiteCookieAttributeNoneSecure()
```

## Documentation

```text
Test SameSite attribute = None by default on Secure session cookies.
```

## Code

```php
  function testSameSiteCookieAttributeNoneSecure() {
    $user = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user->uid);
    $headers = array();
    if (\PHP_VERSION_ID >= 70300) {
      // Send our own login POST so that we can pass a custom header to trigger
      // session_test.module to call ini_set('session.cookie_samesite', $value)
      $headers[] = 'X-Session-Cookie-Ini-Set: None';
    }
    // Test HTTPS session handling by altering the form action to submit the
    // login form through https.php, which creates a mock HTTPS request.
    $this->drupalGet('user');
    $form = $this->xpath('//form[@id="user-login"]');
    $form[0]['action'] = $this->httpsUrl('user');
    $edit = array('name' => $user->name, 'pass' => $user->pass_raw);
    $this->drupalPost(NULL, $edit, t('Log in'), array(), $headers);
    $this->assertTrue(preg_match('/SameSite=None/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie is set as SameSite=None.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
