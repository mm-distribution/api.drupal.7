# SessionTestCase::testSameSiteCookieAttributeNone()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 360–366 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L360-L366)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSameSiteCookieAttributeNone()
```

## Documentation

```text
Test SameSite attribute = None on session cookies.
```

## Code

```php
  function testSameSiteCookieAttributeNone() {
    variable_set('samesite_cookie_value', 'None');
    $user = $this->drupalCreateUser(array('access content'));
    $this->sessionReset($user->uid);
    $this->drupalLogin($user);
    $this->assertTrue(preg_match('/SameSite=None/i', $this->drupalGetHeader('Set-Cookie', TRUE)), 'Session cookie is set as SameSite=None.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
